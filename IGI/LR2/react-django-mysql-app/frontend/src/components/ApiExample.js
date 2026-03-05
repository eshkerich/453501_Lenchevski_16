import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

// Настройка axios для отправки cookies
axios.defaults.withCredentials = true;
// Отключаем автоматическую отправку CSRF токена, будем отправлять вручную
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

function ApiExample() {
  const [items, setItems] = useState([]);
  const [newItem, setNewItem] = useState({ name: '', description: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [user, setUser] = useState(null);
  const [loginForm, setLoginForm] = useState({ username: '', password: '' });
  const [showLogin, setShowLogin] = useState(false);

  useEffect(() => {
    fetchItems();
    checkAuth();
  }, []);

  const getCsrfToken = () => {
    const name = 'csrftoken';
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };

  const checkAuth = async () => {
    try {
      const response = await axios.get(`${API_URL}/auth/user/`);
      setUser(response.data);
      console.log('User authenticated:', response.data);
    } catch (err) {
      console.log('Not authenticated');
      setUser(null);
    }
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    
    try {
      const response = await axios.post(`${API_URL}/auth/login/`, loginForm);
      
      if (response.data.success) {
        setUser(response.data.user);
        setShowLogin(false);
        setLoginForm({ username: '', password: '' });
        setSuccess('Успешный вход');
        fetchItems();
      }
    } catch (err) {
      console.error('Login error:', err);
      setError('Ошибка входа: ' + (err.response?.data?.error || err.message));
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = async () => {
    setLoading(true);
    try {
      await axios.post(`${API_URL}/auth/logout/`);
      setUser(null);
      setSuccess('Выход выполнен');
      fetchItems();
    } catch (err) {
      console.error('Logout error:', err);
      setError('Ошибка при выходе: ' + (err.response?.data?.error || err.message));
    } finally {
      setLoading(false);
    }
  };

  const fetchItems = async () => {
    try {
      const response = await axios.get(`${API_URL}/items/`);
      setItems(response.data);
    } catch (err) {
      console.error('Fetch error:', err);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!newItem.name.trim()) {
      setError('Название не может быть пустым');
      return;
    }
    
    if (!user) {
      setError('Необходимо войти в систему');
      setShowLogin(true);
      return;
    }
    
    setLoading(true);
    setError('');
    setSuccess('');
    
    try {
      // Получаем CSRF токен из cookies
      const csrfToken = getCsrfToken();
      
      const response = await axios.post(`${API_URL}/items/`, newItem, {
        headers: {
          'X-CSRFToken': csrfToken
        }
      });
      setItems([...items, response.data]);
      setNewItem({ name: '', description: '' });
      setSuccess('Элемент создан');
    } catch (err) {
      console.error('Create error:', err);
      if (err.response?.status === 403) {
        setError('Ошибка авторизации. Попробуйте выйти и войти снова.');
        checkAuth();
      } else {
        setError('Ошибка при создании: ' + (err.response?.data?.detail || err.message));
      }
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    if (!user) {
      setError('Необходимо войти в систему');
      setShowLogin(true);
      return;
    }
    
    if (!window.confirm('Удалить элемент?')) return;
    
    try {
      const csrfToken = getCsrfToken();
      await axios.delete(`${API_URL}/items/${id}/`, {
        headers: {
          'X-CSRFToken': csrfToken
        }
      });
      setItems(items.filter(item => item.id !== id));
      setSuccess('Элемент удален');
    } catch (err) {
      console.error('Delete error:', err);
      setError('Ошибка при удалении');
    }
  };

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
      {/* Шапка */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        padding: '10px 20px',
        backgroundColor: '#f0f0f0',
        borderRadius: '8px',
        marginBottom: '20px'
      }}>
        <div>
          <strong>Статус:</strong> {user ? `Вы вошли как ${user.username}` : 'Вы не авторизованы'}
        </div>
        {!user ? (
          <button onClick={() => setShowLogin(!showLogin)} style={styles.button}>
            {showLogin ? 'Отмена' : 'Войти'}
          </button>
        ) : (
          <button onClick={handleLogout} style={styles.buttonLogout} disabled={loading}>
            {loading ? 'Выход...' : 'Выйти'}
          </button>
        )}
      </div>

      {/* Форма входа */}
      {showLogin && !user && (
        <form onSubmit={handleLogin} style={styles.form}>
          <h3>Вход в систему</h3>
          <input
            type="text"
            placeholder="Логин"
            value={loginForm.username}
            onChange={(e) => setLoginForm({...loginForm, username: e.target.value})}
            style={styles.input}
          />
          <input
            type="password"
            placeholder="Пароль"
            value={loginForm.password}
            onChange={(e) => setLoginForm({...loginForm, password: e.target.value})}
            style={styles.input}
          />
          <button type="submit" disabled={loading} style={styles.buttonLogin}>
            {loading ? 'Вход...' : 'Войти'}
          </button>
        </form>
      )}

      <h2>Управление элементами</h2>
      
      {error && <div style={styles.error}>{error}</div>}
      {success && <div style={styles.success}>{success}</div>}
      
      {/* Форма создания */}
      <form onSubmit={handleSubmit} style={styles.form}>
        <h3>Создать новый элемент</h3>
        <input
          type="text"
          placeholder="Название"
          value={newItem.name}
          onChange={(e) => setNewItem({ ...newItem, name: e.target.value })}
          style={styles.input}
          disabled={!user}
        />
        <textarea
          placeholder="Описание"
          value={newItem.description}
          onChange={(e) => setNewItem({ ...newItem, description: e.target.value })}
          style={styles.textarea}
          disabled={!user}
        />
        <button 
          type="submit" 
          disabled={!user || loading}
          style={!user ? styles.buttonDisabled : styles.button}
        >
          {loading ? 'Создание...' : 'Создать'}
        </button>
      </form>
      
      {/* Список элементов */}
      <h3>Элементы ({items.length})</h3>
      {items.map(item => (
        <div key={item.id} style={styles.item}>
          <div>
            <strong>{item.name}</strong>
            {item.description && <p>{item.description}</p>}
            <small>{new Date(item.created_at).toLocaleString()}</small>
          </div>
          {user && (
            <button onClick={() => handleDelete(item.id)} style={styles.deleteButton}>
              Удалить
            </button>
          )}
        </div>
      ))}
    </div>
  );
}

const styles = {
  button: {
    padding: '8px 16px',
    backgroundColor: '#007bff',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer'
  },
  buttonLogout: {
    padding: '8px 16px',
    backgroundColor: '#dc3545',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer'
  },
  buttonLogin: {
    padding: '10px 20px',
    backgroundColor: '#28a745',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer'
  },
  buttonDisabled: {
    padding: '10px 20px',
    backgroundColor: '#ccc',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    cursor: 'not-allowed'
  },
  deleteButton: {
    padding: '5px 10px',
    backgroundColor: '#dc3545',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer'
  },
  form: {
    padding: '20px',
    backgroundColor: '#f9f9f9',
    borderRadius: '8px',
    marginBottom: '20px'
  },
  input: {
    width: '100%',
    padding: '10px',
    marginBottom: '10px',
    border: '1px solid #ddd',
    borderRadius: '4px',
    boxSizing: 'border-box'
  },
  textarea: {
    width: '100%',
    padding: '10px',
    marginBottom: '10px',
    border: '1px solid #ddd',
    borderRadius: '4px',
    minHeight: '80px',
    boxSizing: 'border-box'
  },
  error: {
    color: '#721c24',
    padding: '10px',
    backgroundColor: '#f8d7da',
    border: '1px solid #f5c6cb',
    borderRadius: '4px',
    marginBottom: '20px'
  },
  success: {
    color: '#155724',
    padding: '10px',
    backgroundColor: '#d4edda',
    border: '1px solid #c3e6cb',
    borderRadius: '4px',
    marginBottom: '20px'
  },
  item: {
    padding: '15px',
    backgroundColor: '#f9f9f9',
    border: '1px solid #ddd',
    borderRadius: '4px',
    marginBottom: '10px',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center'
  }
};

export default ApiExample;