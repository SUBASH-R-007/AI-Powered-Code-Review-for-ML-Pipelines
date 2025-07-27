import { useState, useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { useMutation } from "@tanstack/react-query";
import { Cloud, Play, FileText, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import type { Analysis } from "../pages/dashboard"; // Import type from dashboard

interface FileUploadProps {
  onAnalysisStart: () => void;
  onAnalysisComplete: (result: Analysis) => void;
  isLoading: boolean;
}

// Helper function to make the API request
async function startAnalysis(formData: FormData): Promise<Analysis> {
    const response = await fetch('http://localhost:5001/api/analysis', {
        method: 'POST',
        body: formData,
    });

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Analysis failed');
    }

    return response.json();
}


export default function FileUpload({ onAnalysisStart, onAnalysisComplete, isLoading }: FileUploadProps) {
  const [file, setFile] = useState<File | null>(null);

  const uploadMutation = useMutation({
    mutationFn: startAnalysis,
    onSuccess: (data) => {
      // When the backend returns a result, call the function from the dashboard
      onAnalysisComplete(data);
    },
    onError: (error) => {
      console.error("Analysis failed:", error);
      alert(`Analysis Failed: ${error.message}`);
      onAnalysisComplete(null as any); // Reset loading state on parent
    },
  });

  const onDrop = useCallback((acceptedFiles: File[]) => {
    if (acceptedFiles.length > 0) {
      setFile(acceptedFiles[0]);
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { 'text/x-python': ['.py'] },
    multiple: false,
  });
  
  const handleSubmit = () => {
      if (!file) return;
      onAnalysisStart();
      const formData = new FormData();
      formData.append('file', file);
      uploadMutation.mutate(formData);
  }

  const handleRemoveFile = () => {
      setFile(null);
  }

  return (
    <Card className="shadow-lg">
      <CardContent className="p-8">
        <div
          {...getRootProps()}
          className={`relative flex flex-col items-center justify-center w-full p-10 border-2 border-dashed rounded-lg cursor-pointer hover:bg-gray-50
            ${isDragActive ? "border-blue-500 bg-blue-50" : "border-gray-300"}`}
        >
          <input {...getInputProps()} />
          <Cloud className="w-12 h-12 text-gray-400" />
          <p className="mt-4 text-sm text-gray-600">
            {isDragActive ? "Drop the file here..." : "Drag & drop a Python file, or click to select"}
          </p>
          <p className="text-xs text-gray-500">.py files only</p>
        </div>

        {file && (
            <div className="mt-6 flex items-center justify-between p-3 bg-gray-100 rounded-lg">
                <div className="flex items-center space-x-3">
                    <FileText className="h-5 w-5 text-gray-600"/>
                    <span className="text-sm font-medium text-gray-800">{file.name}</span>
                </div>
                <button onClick={handleRemoveFile} className="p-1 rounded-full hover:bg-gray-200">
                    <X className="h-4 w-4 text-gray-500"/>
                </button>
            </div>
        )}

        {isLoading && (
          <div className="mt-6">
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm text-gray-600">Analyzing...</span>
            </div>
            <Progress value={undefined} className="w-full animate-pulse" />
          </div>
        )}

        <Button 
          onClick={handleSubmit}
          disabled={!file || isLoading}
          className="w-full mt-6 bg-blue-600 text-white hover:bg-blue-700 text-lg py-6"
        >
          <Play className="w-5 h-5 mr-2" />
          {isLoading ? "Analyzing..." : "Start Analysis"}
        </Button>
      </CardContent>
    </Card>
  );
}
