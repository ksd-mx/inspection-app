'use client'

import { FirebaseProvider } from './firebase-provider'
import { ReduxProvider } from './redux-provider'

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <FirebaseProvider>
      <ReduxProvider>
        {children}
      </ReduxProvider>
    </FirebaseProvider>
  )
}