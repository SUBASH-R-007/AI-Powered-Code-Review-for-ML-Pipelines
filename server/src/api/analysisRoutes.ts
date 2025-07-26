import { Router } from 'express';
import multer from 'multer';
import { spawn } from 'child_process';
import path from 'path';
import fs from 'fs';

const router = Router();

// Ensure the 'uploads' directory exists to prevent crashes
const uploadsDir = path.join(__dirname, '..', '..', 'uploads');
if (!fs.existsSync(uploadsDir)) {
  fs.mkdirSync(uploadsDir, { recursive: true });
}

// Configure temporary storage for uploaded files
const upload = multer({ dest: uploadsDir });

router.post('/', upload.single('file'), (req, res) => {
  console.log('=== ANALYSIS REQUEST RECEIVED ===');
  
  if (!req.file) {
    console.log('ERROR: No file uploaded');
    return res.status(400).json({ error: 'No file was uploaded.' });
  }

  const uploadedFilePath = req.file.path;
  console.log('Uploaded file path:', uploadedFilePath);
  
  // CORRECTED: The path should be one level up, then ml_analyzer
  const pythonBridgeScript = path.join(__dirname, '..', 'ml_analyzer', 'main.py');
  
  console.log('Python script path:', pythonBridgeScript);
  console.log('Python script exists:', fs.existsSync(pythonBridgeScript));
  console.log('Current __dirname:', __dirname);

  if (!fs.existsSync(pythonBridgeScript)) {
    console.error('CRITICAL ERROR: Python script not found!');
    return res.status(500).json({ 
      error: 'Python analysis script not found',
      details: `Script path: ${pythonBridgeScript}`
    });
  }

  // Use 'py' on Windows for reliability, fallback to 'python'
  const pythonCommand = process.platform === 'win32' ? 'py' : 'python';
  console.log('Python command:', pythonCommand);
  console.log('Platform:', process.platform);
  
  const pythonProcess = spawn(pythonCommand, [pythonBridgeScript, uploadedFilePath]);

  let analysisResultJson = '';
  let errorOutput = '';

  pythonProcess.stdout.on('data', (data) => {
    console.log('Python stdout:', data.toString());
    analysisResultJson += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    console.log('Python stderr:', data.toString());
    errorOutput += data.toString();
  });

  pythonProcess.on('error', (error) => {
    console.error('Failed to start Python process:', error);
    fs.unlinkSync(uploadedFilePath); // Clean up
    return res.status(500).json({
      error: 'Failed to start Python analysis process',
      details: error.message
    });
  });

  pythonProcess.on('close', (code) => {
    console.log(`Python process exited with code: ${code}`);
    fs.unlinkSync(uploadedFilePath); // Clean up the uploaded file

    if (code !== 0) {
      console.error("--- PYTHON SCRIPT FAILED ---");
      console.error(`Exit Code: ${code}`);
      console.error("Error Output:", errorOutput);
      console.error("--- END PYTHON ERROR ---");

      return res.status(500).json({
        error: 'The analysis script encountered an internal error.',
        details: errorOutput,
        exitCode: code
      });
    }

    console.log('Raw Python output:', analysisResultJson);

    try {
      const results = JSON.parse(analysisResultJson);
      console.log('Parsed results successfully');
      res.status(200).json(results);
    } catch (e) {
      console.error('Failed to parse JSON:', e);
      res.status(500).json({
        error: 'Failed to parse the JSON results from the script.',
        rawOutput: analysisResultJson
      });
    }
  });
});

export default router;