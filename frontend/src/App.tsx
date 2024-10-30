import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import Dashboard from './pages/Dashboard';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="flex h-screen">
        <div className="flex-1 flex flex-col overflow-hidden">
          <Dashboard />
        </div>
      </div>
    </QueryClientProvider>
  );
}

export default App;
