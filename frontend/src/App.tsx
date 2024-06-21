import { Outlet } from 'react-router-dom';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col justify-center items-center">
      <Outlet />
    </div>
  );
}

export default App;
