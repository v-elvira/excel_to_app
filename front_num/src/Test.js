import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './SalesTable.css';

function Test() {
  const [sales, setSales] = useState([]);
  const [sortConfig, setSortConfig] = useState({ key: 'delivery_date', direction: null });

  const handleSort = (key) => {
    let direction = 'asc';
    if (sortConfig.key === key && sortConfig.direction === 'asc') {
      direction = 'desc';
    }
    setSortConfig({ key, direction });
  };

  const sortedSales = [...sales].sort((a, b) => {
    if (a[sortConfig.key] < b[sortConfig.key]) {
      return sortConfig.direction === 'asc' ? -1 : 1;
    }
    if (a[sortConfig.key] > b[sortConfig.key]) {
      return sortConfig.direction === 'asc' ? 1 : -1;
    }
    return 0;
  });

  useEffect(() => {
    fetchSales();
    const intervalId = setInterval(fetchSales, 5000);
    return () => clearInterval(intervalId);
  }, []);

  const fetchSales = () => {
    axios.get('http://localhost:8000')
      // .then(res => setSales(res.data))
      .then(res => {
        // sort data by delivery_date for the initial rendering
        const sortedData = res.data.sort((a, b) => new Date(a.delivery_date) - new Date(b.delivery_date));
        setSales(sortedData);
      })
      .catch(err => console.log(err));
  };


  // Format a number as currency using the default locale settings
  const formatCurrency = (value, currency = 'RUB') => {
    return value.toLocaleString(undefined, { style: 'currency', currency: currency});
  };

    // Function to add the 'active' class to the table header cell for the current sort key
  const getHeaderClass = (key) => {
    if (sortConfig.key === key) {
      return 'active';
    }
    return '';
  };

  return (
    <div>
    <h1 className='center'> Активные заказы: </h1>
      <table className="sales-table">
      <thead>
        <tr>
          <th onClick={() => handleSort('id')} className={getHeaderClass('id')}>ID</th>
          <th onClick={() => handleSort('delivery_date')} className={getHeaderClass('delivery_date')}>Дата поставки</th>
          <th onClick={() => handleSort('price')} className={`number ${getHeaderClass('price')}`}>Цена</th>
          <th onClick={() => handleSort('rub_price')}  className={`number ${getHeaderClass('rub_price')}`}>В рублях по текущему курсу</th>
        </tr>
      </thead>
      <tbody>
        {sortedSales.map((sale) => (
          <tr key={sale.id}>
            <td>{sale.id}</td>
            <td>{sale.delivery_date}</td>
            <td className='number'>{formatCurrency(sale.price, 'USD')}</td>
            <td className='number'>{formatCurrency(sale.rub_price)}</td>
          </tr>
        ))}
      </tbody>
    </table>
    </div>
  );
}

export default Test;