import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { TooltipProvider } from "@/components/ui/tooltip";
import Dashboard from "@/pages/dashboard";

// Create the query client instance
const queryClient = new QueryClient();

function App() {
  return (
    // The QueryClientProvider is still needed for useMutation in the file upload component
    <QueryClientProvider client={queryClient}>
      <TooltipProvider>
        {/* We directly render the Dashboard now, no more complex routing */}
        <Dashboard />
      </TooltipProvider>
    </QueryClientProvider>
  );
}

export default App;
