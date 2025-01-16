'use client'

import { useEffect, useState } from 'react'
import { getApps, initializeApp } from 'firebase/app'
import { getFirestore } from 'firebase/firestore'
import { firebaseConfig } from '@/infrastructure/persistence/firebase/config'

export function FirebaseProvider({ children }: { children: React.ReactNode }) {
  const [initialized, setInitialized] = useState(false)

  useEffect(() => {
    if (getApps().length === 0) {
      const app = initializeApp(firebaseConfig)
      // Initialize Firestore
      getFirestore(app)
    }
    setInitialized(true)
  }, [])

  if (!initialized) {
    return <div>Loading...</div>
  }

  return <>{children}</>
}