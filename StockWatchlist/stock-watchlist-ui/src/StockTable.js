import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const StockTable = () => {
  const [stockData, setStockData] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    axios.get('http://127.0.0.1:4000/api/getCompaniesStockInfo')
      .then(response => {
        setStockData(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the stock data!", error);
      });
  }, []);

  const handleRowClick = (companyName) => {
    navigate(`/stock/${companyName}`);
  };

  return (
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Market Cap</th>
          <th>LTP</th>
          <th>1D Change</th>
          <th>1W Change</th>
          <th>1Month Change</th>
          <th>1Year Change</th>
          <th>P/E</th>
          <th>5Yrs PE</th>
          <th>Down from 52w High</th>
        </tr>
      </thead>
      <tbody>
        {stockData.map((stock, index) => {
          const company = Object.keys(stock)[0];
          const data = stock[company];

          if (typeof data === 'string') {
            return (
              <tr key={index}>
                <td>{company}</td>
                <td colSpan="9">{data}</td>
              </tr>
            );
          }

          return (
            <tr key={index} onClick={() => handleRowClick(data.sid)}>
              <td>{company}</td>
              <td>{data.technicals.marketCap}</td>
              <td>{data.technicals.ltp}</td>
              <td>{data.returns["1DayReturns"]}</td>
              <td>{data.returns["1WeekReturns"]}</td>
              <td>{data.returns["1MonthReturns"]}</td>
              <td>{data.returns["1YearReturns"]}</td>
              <td>{data.technicals.pe}</td>
              <td>{data.technicals.pb}</td>
              <td>{((data.technicals['52wHigh'] - data.technicals.ltp) / data.technicals['52wHigh'] * 100).toFixed(2)}%</td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}

export default StockTable;
