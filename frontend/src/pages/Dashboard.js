import React from 'react';
import { Container, Box, Typography } from '@mui/material';

const Dashboard = () => {
  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Box sx={{ mb: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Instapy Dashboard
        </Typography>
        <Typography variant="body1" color="textSecondary">
          Advanced Instagram OSINT Analysis Platform
        </Typography>
      </Box>
    </Container>
  );
};

export default Dashboard;
