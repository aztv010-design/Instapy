import { configureStore } from '@reduxjs/toolkit';
import profileReducer from './slices/profileSlice';
import analysisReducer from './slices/analysisSlice';
import reportReducer from './slices/reportSlice';

export const store = configureStore({
  reducer: {
    profile: profileReducer,
    analysis: analysisReducer,
    report: reportReducer,
  },
});
