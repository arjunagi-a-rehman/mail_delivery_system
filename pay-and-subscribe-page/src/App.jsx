import PayPage from "./components/PayPage"
import { Route, Routes } from "react-router-dom";


function App() {

  return (
    <Routes>
      <Route path="/users/:userId" element={<PayPage />} />
    </Routes>
  );
}

export default App
