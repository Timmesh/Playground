import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const SearchBox = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [isTyping, setIsTyping] = useState(false);
  const navigate = useNavigate();

  const fetchResults = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:4000/api/search?query=${query}`);
      setResults(response.data.data.stocks || []);
    } catch (error) {
      console.error('Error fetching search results:', error);
    }
  };

  const handleChange = (e) => {
    setQuery(e.target.value);
    setIsTyping(true);
  };

  React.useEffect(() => {
    if (query) {
      const timerId = setTimeout(() => {
        fetchResults();
      }, 3000);

      return () => clearTimeout(timerId);
    }
  }, [query]);

  const handleSelect = (result) => {
    navigate(`/stock/${result.sid}`);
    setQuery('');
    setIsTyping(false);
  };

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={handleChange}
        placeholder="Search for a stock"
      />
      {isTyping && query && (
        <ul>
          {results.map((result) => (
            <li key={result.sid} onClick={() => handleSelect(result)}>{result.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default SearchBox;
