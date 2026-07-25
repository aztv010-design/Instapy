import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const NetworkAnalysis = () => {
  return (
    <Container>
      <Box sx={{ py: 4 }}>
        <Typography variant="h4">Network Analysis</Typography>
        <Typography variant="body1" sx={{ mt: 2 }}>
          Analyze relationships and networks between Instagram accounts.
        </Typography>
      </Box>
    </Container>
  );
};

export default NetworkAnalysis;
