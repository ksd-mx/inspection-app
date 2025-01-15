import { getInspection } from '@/core/application/services/inspection.service'

export default async function InspectionPage({
  params,
}: {
  params: { id: string }
}) {
  const inspection = await getInspection(params.id)

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">{inspection.title}</h1>
      <div className="bg-white p-6 rounded-lg shadow">
        <p className="text-gray-600">Status: {inspection.status}</p>
      </div>
    </div>
  )
}