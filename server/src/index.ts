import express from 'express';
import cors from 'cors';
import path from 'path';
import analysisRoutes from './api/analysisRoutes';

const app = express();
const PORT = process.env.PORT || 5001;

// Middleware
app.use(cors({
  origin: 'http://localhost:5173', // Your React dev server
  credentials: true
}));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.use('/api/analysis', analysisRoutes);

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'OK', message: 'Server is running' });
});

// Serve static files from uploads directory (if needed)
app.use('/uploads', express.static(path.join(__dirname, '../uploads')));

// Start server
app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
  console.log(`📊 Analysis API available at http://localhost:${PORT}/api/analysis`);
});

export default app;