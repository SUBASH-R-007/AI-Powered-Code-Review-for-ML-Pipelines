import { CheckCircle, AlertCircle, AlertTriangle, Info } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
// CORRECTED: Import types from the dashboard page
import type { Analysis, AnalysisIssue } from "../pages/dashboard";

interface AnalysisResultsProps {
  analysis: Analysis;
}

export default function AnalysisResults({ analysis }: AnalysisResultsProps) {
  const issues: AnalysisIssue[] = analysis?.issues || [];

  const getIssueIcon = (severity: string) => {
    switch (severity) {
      case 'critical':
        return <AlertCircle className="h-5 w-5 text-red-500" />;
      case 'warning':
        return <AlertTriangle className="h-5 w-5 text-orange-500" />;
      default:
        return <Info className="h-5 w-5 text-blue-500" />;
    }
  };

  const getIssueBadgeColor = (severity: string) => {
    switch (severity) {
      case 'critical':
        return "bg-red-100 text-red-800";
      case 'warning':
        return "bg-orange-100 text-orange-800";
      default:
        return "bg-blue-100 text-blue-800";
    }
  };
  
  const getIssueBorderColor = (severity: string) => {
    switch (severity) {
      case 'critical':
        return "border-red-200";
      case 'warning':
        return "border-orange-200";
      default:
        return "border-blue-200";
    }
  };

  return (
    <Card>
      <CardContent className="p-6">
        <h3 className="text-xl font-semibold mb-4">Analysis Report</h3>
        <div className="space-y-4">
          {issues.length === 0 ? (
            <div className="flex flex-col items-center justify-center text-center p-8 bg-green-50 rounded-lg">
                <CheckCircle className="h-12 w-12 text-green-500 mb-4"/>
                <h4 className="text-lg font-medium text-green-800">Excellent!</h4>
                <p className="text-sm text-green-700">No issues were detected in your code.</p>
            </div>
          ) : (
            issues.map((issue) => (
              <div key={issue.id} className={`p-4 border-l-4 rounded-r-lg ${getIssueBorderColor(issue.severity)} bg-gray-50`}>
                <div className="flex items-start space-x-4">
                  <div className="flex-shrink-0 mt-1">
                    {getIssueIcon(issue.severity)}
                  </div>
                  <div className="flex-1">
                    <div className="flex items-center justify-between">
                      <h4 className="font-medium text-gray-900">{issue.title}</h4>
                      <Badge className={`text-xs font-semibold ${getIssueBadgeColor(issue.severity)}`}>
                        {issue.severity}
                      </Badge>
                    </div>
                    <p className="text-sm text-gray-700 mt-1">{issue.description}</p>
                    <div className="mt-2 text-xs text-gray-600">
                      <span>Lines {issue.lineStart}-{issue.lineEnd}</span>
                    </div>
                    {issue.suggestions && (
                      <div className="mt-3 text-sm text-green-800 bg-green-100 p-3 rounded-md">
                        <strong>Suggestion:</strong> {issue.suggestions}
                      </div>
                    )}
                  </div>
                </div>
              </div>
            ))
          )}
        </div>
      </CardContent>
    </Card>
  );
}
