import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const Settings = () => {
  return (
    <Container>
      <Box sx={{ py: 4 }}>
        <Typography variant="h4">Settings</Typography>
        <Typography variant="body1" sx={{ mt: 2 }}>
          Configure your Instapy settings here.
        </Typography>
      </Box>
    </Container>
  );
};

export default Settings;
