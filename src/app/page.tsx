import { getInspections } from '@/core/application/services/inspection.service'

export default async function Home() {
  // Mock data - will be replaced with actual service call later
  const inspections = await getInspections()

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Inspector&apos;s Vault</h1>
      <div className="grid gap-4">
        {inspections.map((inspection) => (
          <div key={inspection.id} className="p-4 border rounded">
            <h2 className="text-xl">{inspection.title}</h2>
            <p className="text-gray-600">{inspection.status}</p>
          </div>
        ))}
      </div>
    </div>
  )
}