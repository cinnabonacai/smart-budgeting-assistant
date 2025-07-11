import React, { useEffect, useState } from "react";
import { Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

const Dashboard = () => {
  const [summary, setSummary] = useState({});
  const [transactions, setTransactions] = useState([]);
  const [month, setMonth] = useState(6); // Default to June
  const [year, setYear] = useState(2025);

  useEffect(() => {
    fetchSummary();
    fetchTransactions();
  }, [month, year]);

  const fetchSummary = async () => {
    const res = await fetch(
      `http://127.0.0.1:8000/suggestions/summary?month=${month}&year=${year}`
    );
    const data = await res.json();
    setSummary(data);
  };

  const fetchTransactions = async () => {
    const res = await fetch(
      `http://127.0.0.1:8000/suggestions/categorized?month=${month}&year=${year}`
    );
    const data = await res.json();
    setTransactions(data);
  };

  const pieData = {
    labels: Object.keys(summary),
    datasets: [
      {
        label: "Spending ($)",
        data: Object.values(summary).map((amt) => Math.abs(amt)),
        backgroundColor: [
          "#FF6384",
          "#36A2EB",
          "#FFCE56",
          "#4BC0C0",
          "#9966FF",
          "#FF9F40",
        ],
      },
    ],
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Smart Budgeting Dashboard</h1>

      <div className="mb-4 flex gap-4">
        <select
          className="p-2 border"
          value={month}
          onChange={(e) => setMonth(Number(e.target.value))}
        >
          {[...Array(12).keys()].map((m) => (
            <option key={m + 1} value={m + 1}>
              {m + 1}
            </option>
          ))}
        </select>

        <select
          className="p-2 border"
          value={year}
          onChange={(e) => setYear(Number(e.target.value))}
        >
          {[2024, 2025, 2026].map((y) => (
            <option key={y} value={y}>
              {y}
            </option>
          ))}
        </select>
      </div>

      <div className="mb-6 w-1/2">
        <Pie data={pieData} />
      </div>

      <table className="w-full border">
        <thead>
          <tr className="bg-gray-200">
            <th className="p-2 border">Date</th>
            <th className="p-2 border">Merchant</th>
            <th className="p-2 border">Amount</th>
            <th className="p-2 border">Category</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((txn) => (
            <tr key={txn.transaction_id}>
              <td className="p-2 border">{txn.date}</td>
              <td className="p-2 border">{txn.merchant}</td>
              <td className="p-2 border">${txn.amount.toFixed(2)}</td>
              <td className="p-2 border">{txn.category}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Dashboard;

