import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const StockInfo = () => {
  const { id } = useParams();
  const [info, setInfo] = useState(null);

  useEffect(() => {
    const fetchStockInfo = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:4000/api/getStockInfo/${id}`);
        setInfo(response.data);
      } catch (error) {
        console.error('Error fetching stock info:', error);
      }
    };

    fetchStockInfo();
  }, [id]);

  if (!info) return <div>Loading...</div>;

  return (
    <div>
      <h2>{info.name}</h2>
      <p>{info.description}</p>
      <p>Market Cap: {info.technicals.marketCap}</p>
      <p>LTP: {info.technicals.ltp}</p>
      <p>1 Day Change: {info.returns['1DayReturns']}</p>
      <p>1 Week Change: {info.returns['1WeekReturns']}</p>
      <p>1 Month Change: {info.returns['1MonthReturns']}</p>
      <p>1 Year Change: {info.returns['1YearReturns']}</p>
      <p>P/E: {info.technicals.pe}</p>
      <p>5 Years PE: {info.technicals.pb}</p>
      <p>Down from 52w High: {info.technicals['52wHigh'] - info.technicals.ltp}</p>
    </div>
  );
};

export default StockInfo;
