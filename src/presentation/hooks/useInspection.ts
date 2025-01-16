import { useEffect } from 'react'
import { useAppDispatch, useAppSelector } from '../state/store'
import { 
  setLoading, 
  updateInspection, 
  setError,
  selectInspectionById
} from '../state/slices/inspection.slice'
import { getFirestore, doc, onSnapshot } from 'firebase/firestore'
import { getApps } from 'firebase/app'

export function useInspection(inspectionId: string) {
  const dispatch = useAppDispatch()
  const inspection = useAppSelector(state => selectInspectionById(state, inspectionId))

  useEffect(() => {
    // Check if Firebase is initialized
    if (getApps().length === 0) {
      dispatch(setError('Firebase not initialized'))
      return
    }

    dispatch(setLoading(true))
    
    try {
      const db = getFirestore()
      const inspectionRef = doc(db, 'inspections', inspectionId)

      const unsubscribe = onSnapshot(inspectionRef, 
        (snapshot) => {
          if (snapshot.exists()) {
            dispatch(updateInspection({
              id: snapshot.id,
              ...snapshot.data()
            }))
          }
          dispatch(setLoading(false))
        },
        (error) => {
          console.error('Error fetching inspection:', error)
          dispatch(setError(error.message))
          dispatch(setLoading(false))
        }
      )

      return () => unsubscribe()
    } catch (error) {
      console.error('Error setting up Firebase listener:', error)
      dispatch(setError(error instanceof Error ? error.message : 'Unknown error'))
      dispatch(setLoading(false))
    }
  }, [inspectionId, dispatch])

  return {
    inspection,
    loading: useAppSelector(state => state.inspection.loading),
    error: useAppSelector(state => state.inspection.error)
  }
}