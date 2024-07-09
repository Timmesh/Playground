import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import StockTable from './components/StockTable';
import StockInfo from './pages/StockInfo';
import SearchBox from './components/SearchBox';
import './styles/App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <h1>Stock Watchlist</h1>
        <SearchBox />
        <Routes>
          <Route exact path="/" element={<StockTable />} />
          <Route path="/stock/:id" element={<StockInfo />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
