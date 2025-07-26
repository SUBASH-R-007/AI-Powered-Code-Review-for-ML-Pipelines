import { Bug, AlertTriangle, Clock, Target } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
// CORRECTED: Import the 'Analysis' type from the dashboard page
import type { Analysis } from "../pages/dashboard";

interface MetricsOverviewProps {
  analysis: Analysis;
}

export default function MetricsOverview({ analysis }: MetricsOverviewProps) {
  const metrics = [
    {
      title: "Overall Score",
      value: analysis.overallScore,
      icon: Target,
      bgColor: "bg-indigo-50",
      iconColor: "text-indigo-500",
    },
    {
      title: "Critical Issues",
      value: analysis.criticalIssues,
      icon: Bug,
      bgColor: "bg-red-50",
      iconColor: "text-red-500",
    },
    {
      title: "Warnings",
      value: analysis.warnings,
      icon: AlertTriangle,
      bgColor: "bg-orange-50",
      iconColor: "text-orange-500",
    },
    {
      title: "Performance",
      value: analysis.performanceIssues,
      icon: Clock,
      bgColor: "bg-blue-50",
      iconColor: "text-blue-500",
    },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      {metrics.map((metric, index) => (
        <Card key={index} className="shadow-sm">
          <CardContent className="p-6">
            <div className="flex items-center">
              <div className={`w-10 h-10 ${metric.bgColor} rounded-lg flex items-center justify-center`}>
                <metric.icon className={`h-6 w-6 ${metric.iconColor}`} />
              </div>
              <div className="ml-4">
                <p className="text-sm text-gray-500">{metric.title}</p>
                <p className="text-2xl font-bold text-gray-900">{metric.value}</p>
              </div>
            </div>
          </CardContent>
        </Card>
      ))}
    </div>
  );
}
