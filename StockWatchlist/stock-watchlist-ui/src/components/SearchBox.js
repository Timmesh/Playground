import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { fetchResults } from '../utils/api';

const SearchBox = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [isTyping, setIsTyping] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setQuery(e.target.value);
    setIsTyping(true);
  };

  useEffect(() => {
    if (query) {
      const timerId = setTimeout(() => {
        fetchResults(query).then(setResults);
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
