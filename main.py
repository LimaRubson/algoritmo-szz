import React, { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';
import Commit from './components/pages/Commit';
import Ia from './components/pages/Ia';
import Home from './components/pages/Home';
import LandingPage from './components/pages/LandingPage';
import LoginPage from './components/pages/LoginPage';
import RegisterPage from './components/pages/RegisterPage';
import ListUsers from './components/users/Users';
import CreateUser from './components/users/CreateUser';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Config_file from './Config_file';

const App = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const openSidebar = () => {
    setSidebarOpen(true);
  };
  const closeSidebar = () => {
    setSidebarOpen(false);
  };

  const [commits, setCommits] = useState([]);
  const [metrics, setMetrics] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [notification, setNotification] = useState(null);  // Novo estado para armazenar a notificação

  useEffect(() => {
    fetchCommits();
    fetchMetrics();

    // WebSocket connection
    const ws = new WebSocket('ws://localhost:3000');  // Substitua pelo URL correto do WebSocket

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'PREDICTION_RESULT') {
        setNotification(`Commit ${data.commit_id}: Predição Concluída - ${data.prediction}`);
      }
    };

    ws.onclose = () => {
      console.log('WebSocket Disconnected');
    };

   
  }, [);

  const fetchCommits = async () => {
    try {
      
      console.log('Dados recebidos:', 
      setCommits(response.data);
      setLoading(false);
     catch (error) {
      console.error('Erro ao buscar commits:', error.message);
      console.error('Detalhes do erro:', error.response ? error.response.data : 'Sem resposta do servidor');
      setError('Erro ao buscar commits');
      setLoading(false);
    }
  };

  const fetchMetrics = async () => {
    try {
      const response = await axios.get('http://3.94.86.29:8000/api/evaluation_metrics
      console.log('Dados recebidos:, response.data);
      setMetrics(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Erro ao buscar commits:', error.message);
      console.error('Detalhes do erro:', error.response ? error.response.data : 'Sem resposta do servidor');
      setError('Erro ao buscar commits');
      setLoading(false);
    }
  };

  if (loading) {
    return <div>Carregando...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <BrowserRouter>
      <div>
        {notification && <div className="notification>{notification}</div>} {/* Exibe a notificação se existir */}
        <Routes>
          <Route path="/" element={<LandingPage
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/listusers" element={<ListUsers sidebarOpen={sidebarOpen} openSidebar={openSidebar} closeSidebar={closeSidebar} />} />
          <Route path="/addnewuser" element={<CreateUser />} />
          <Route path='/home' element={<Home sidebarOpen={sidebarOpen} openSidebar={openSidebar} closeSidebar={closeSidebar} commits={commits} metrics={metrics} />} />
          <Route path='/commits' element={<Commit sidebarOpen={sidebarOpen} openSidebar={openSidebar} closeSidebar={closeSidebar} commits={commits} metrics={metrics} />} />
          <Route path='/ia' element={<Ia sidebarOpen={sidebarOpen} openSidebar={openSidebar} closeSidebar={closeSidebar} commits={commits} metrics={metrics} />} />
          <Route path='/config' element={<Config_file
          <Route path='*' element={<h1>Not Found
        </Routes>
      </div>
    </BrowserRouter>
  );
};

export default App;
