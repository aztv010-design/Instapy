import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  analyses: [],
  loading: false,
  error: null,
};

const analysisSlice = createSlice({
  name: 'analysis',
  initialState,
  reducers: {
    setAnalyses: (state, action) => {
      state.analyses = action.payload;
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
  },
});

export const { setAnalyses, setLoading } = analysisSlice.actions;
export default analysisSlice.reducer;
