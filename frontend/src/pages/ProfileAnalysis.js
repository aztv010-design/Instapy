import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import {
  Container,
  Paper,
  TextField,
  Button,
  Box,
  CircularProgress,
  Alert,
} from '@mui/material';
import { setProfile, setLoading } from '../store/slices/profileSlice';
import { profileService } from '../services/api';

const ProfileAnalysis = () => {
  const [username, setUsername] = useState('');
  const [loading, setLoadingState] = useState(false);
  const [error, setError] = useState(null);
  const dispatch = useDispatch();

  const handleScan = async () => {
    if (!username.trim()) {
      setError('Please enter a username');
      return;
    }

    setLoadingState(true);
    setError(null);
    dispatch(setLoading(true));

    try {
      const response = await profileService.scanProfile(username);
      dispatch(setProfile(response.data));
    } catch (err) {
      setError(err.response?.data?.detail || 'Error scanning profile');
    } finally {
      setLoadingState(false);
      dispatch(setLoading(false));
    }
  };

  return (
    <Container maxWidth="sm" sx={{ py: 4 }}>
      <Paper sx={{ p: 3 }}>
        <Box sx={{ mb: 2 }}>
          <TextField
            fullWidth
            label="Instagram Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Enter username"
            disabled={loading}
          />
        </Box>
        {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}
        <Button
          fullWidth
          variant="contained"
          onClick={handleScan}
          disabled={loading}
          sx={{ py: 1.5 }}
        >
          {loading ? <CircularProgress size={24} /> : 'Analyze Profile'}
        </Button>
      </Paper>
    </Container>
  );
};

export default ProfileAnalysis;
