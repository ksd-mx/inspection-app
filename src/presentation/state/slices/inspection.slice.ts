import { createSlice, createEntityAdapter, PayloadAction } from '@reduxjs/toolkit'
import type { RootState } from '../store'
import { Inspection } from '@/core/domain/entities/inspection'

export const inspectionsAdapter = createEntityAdapter<Inspection>({
  selectId: (inspection) => inspection.id,
})

export const inspectionSlice = createSlice({
  name: 'inspection',
  initialState: inspectionsAdapter.getInitialState({
    loading: false,
    activeInspectionId: null as string | null,
    error: null as string | null,
  }),
  reducers: {
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload
    },
    setActiveInspection: (state, action: PayloadAction<string>) => {
      state.activeInspectionId = action.payload
    },
    updateInspection: (state, action: PayloadAction<Inspection>) => {
      inspectionsAdapter.upsertOne(state, action.payload)
    },
    setInspections: (state, action: PayloadAction<Inspection[]>) => {
      inspectionsAdapter.setAll(state, action.payload)
    },
    setError: (state, action: PayloadAction<string | null>) => {
      state.error = action.payload
    },
  },
})

export const {
  setLoading,
  setActiveInspection,
  updateInspection,
  setInspections,
  setError,
} = inspectionSlice.actions

// Selectors
export const { selectAll: selectAllInspections, selectById: selectInspectionById } =
  inspectionsAdapter.getSelectors<RootState>((state) => state.inspection)

export default inspectionSlice.reducer