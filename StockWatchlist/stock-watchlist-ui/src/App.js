import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import StockTable from './StockTable';
import StockInfo from './StockInfo';
import SearchBox from './SearchBox';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <h1>Stock Information</h1>
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
