import axios from 'axios';

export const fetchResults = async (query) => {
  try {
    const response = await axios.get(`http://127.0.0.1:4000/api/search?query=${query}`);
    return response.data.data.stocks || [];
  } catch (error) {
    console.error('Error fetching search results:', error);
    return [];
  }
};

export const fetchStockInfo = async (id) => {
  try {
    const response = await axios.get(`http://127.0.0.1:4000/api/getStockInfo/${id}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching stock info:', error);
    return null;
  }
};

export const fetchCompaniesStockInfo = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:4000/api/getCompaniesStockInfo');
    return response.data;
  } catch (error) {
    console.error('Error fetching the stock data!', error);
    return [];
  }
};
