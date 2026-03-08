function ResourceCard({ resource }) {
  return (
    <div className="resource-card">
      <h3>{resource.title}</h3>
      <p className="views">{resource.views.toLocaleString()} views</p>
      <a href={resource.url} target="_blank" rel="noopener noreferrer">
        View Resource →
      </a>
    </div>
  )
}

export default ResourceCard
