interface Inspection {
    id: string
    title: string
    status: string
  }
  
  export async function getInspection(id: string): Promise<Inspection> {
    // Mock return - will be replaced with actual implementation
    return { id, title: `Sample Inspection ${id}`, status: 'In Progress' }
  }
  
  export async function getInspections(): Promise<Inspection[]> {
    // Mock return - will be replaced with actual implementation
    return [
      { id: '1', title: 'Sample Inspection 1', status: 'In Progress' },
      { id: '2', title: 'Sample Inspection 2', status: 'Completed' },
    ]
  }