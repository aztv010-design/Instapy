import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  reports: [],
  loading: false,
};

const reportSlice = createSlice({
  name: 'report',
  initialState,
  reducers: {
    setReports: (state, action) => {
      state.reports = action.payload;
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
  },
});

export const { setReports, setLoading } = reportSlice.actions;
export default reportSlice.reducer;
