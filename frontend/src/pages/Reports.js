import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const Reports = () => {
  return (
    <Container>
      <Box sx={{ py: 4 }}>
        <Typography variant="h4">Reports</Typography>
        <Typography variant="body1" sx={{ mt: 2 }}>
          View and download generated analysis reports.
        </Typography>
      </Box>
    </Container>
  );
};

export default Reports;
