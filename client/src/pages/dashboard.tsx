import { useState } from "react";
import { Code, BarChart3, Settings } from "lucide-react";
import FileUpload from "../components/file-upload";
import AnalysisResults from "../components/analysis-results";
import MetricsOverview from "../components/metrics-overview";

// Define the Analysis type directly, since schema.ts is removed
export interface AnalysisIssue {
  id: string;
  severity: 'critical' | 'warning' | 'info';
  title: string;
  description: string;
  lineStart: number;
  lineEnd: number;
  suggestions?: string;
}

export interface Analysis {
  id: string;
  projectName: string;
  status: string;
  overallScore: number;
  criticalIssues: number;
  warnings: number;
  performanceIssues: number;
  coverage: number;
  createdAt: string;
  issues: AnalysisIssue[];
}


export default function Dashboard() {
  // State to hold the result of the one-time analysis
  const [analysisResult, setAnalysisResult] = useState<Analysis | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  // This function will be called by FileUpload when the analysis is complete
  const handleAnalysisComplete = (result: Analysis) => {
    setAnalysisResult(result);
    setIsLoading(false);
  };
  
  // This function will be called by FileUpload when the analysis starts
  const handleAnalysisStart = () => {
      setIsLoading(true);
      setAnalysisResult(null);
  }

  // Function to start a new analysis, clearing the old result
  const handleNewAnalysis = () => {
    setAnalysisResult(null);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <Code className="h-8 w-8 text-blue-600" />
              <h1 className="text-2xl font-bold text-gray-800">
                ML Code Reviewer
              </h1>
            </div>
            <div className="flex items-center space-x-4">
              <button className="p-2 rounded-full hover:bg-gray-100">
                <BarChart3 className="h-5 w-5 text-gray-600" />
              </button>
              <button className="p-2 rounded-full hover:bg-gray-100">
                <Settings className="h-5 w-5 text-gray-600" />
              </button>
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Conditional Rendering: Show results or upload form */}
        {analysisResult ? (
          // VIEW 2: SHOW ANALYSIS RESULTS
          <div>
            <button
              onClick={handleNewAnalysis}
              className="mb-6 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700"
            >
              Start New Analysis
            </button>
            <MetricsOverview analysis={analysisResult} />
            <AnalysisResults analysis={analysisResult} />
          </div>
        ) : (
          // VIEW 1: SHOW FILE UPLOAD
          <div className="max-w-2xl mx-auto">
             <h2 className="text-center text-3xl font-extrabold text-gray-900">
                Analyze Your ML Code Instantly
            </h2>
            <p className="mt-4 text-center text-md text-gray-600">
                Upload your Python script to get an in-depth review of code quality, performance, and security vulnerabilities.
            </p>
            <div className="mt-8">
                <FileUpload 
                    onAnalysisStart={handleAnalysisStart}
                    onAnalysisComplete={handleAnalysisComplete} 
                    isLoading={isLoading}
                />
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
