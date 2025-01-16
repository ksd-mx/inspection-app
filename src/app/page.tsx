'use client'

import { useEffect } from 'react'
import { useAppDispatch, useAppSelector } from '@/presentation/state/store'
import { setLoading, setInspections, selectAllInspections } from '@/presentation/state/slices/inspection.slice'
import { getInspections } from '@/core/application/services/inspection.service'
import Link from 'next/link'

export default function Home() {
  const dispatch = useAppDispatch()
  const inspections = useAppSelector(selectAllInspections)
  const loading = useAppSelector(state => state.inspection.loading)
  const error = useAppSelector(state => state.inspection.error)

  useEffect(() => {
    async function loadInspections() {
      dispatch(setLoading(true))
      try {
        const data = await getInspections()
        dispatch(setInspections(data))
      } catch (err) {
        console.error('Failed to load inspections:', err)
      } finally {
        dispatch(setLoading(false))
      }
    }

    loadInspections()
  }, [dispatch])

  if (loading) return <div className="p-8">Loading inspections...</div>
  if (error) return <div className="p-8 text-red-500">Error: {error}</div>

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Inspector&apos;s Vault</h1>
      <div className="grid gap-4">
        {inspections.map((inspection) => (
          <Link 
            href={`/inspections/${inspection.id}`} 
            key={inspection.id}
            className="p-4 border rounded hover:bg-gray-50 transition-colors"
          >
            <h2 className="text-xl">{inspection.title}</h2>
            <p className="text-gray-600">{inspection.status}</p>
          </Link>
        ))}
      </div>
    </div>
  )
}