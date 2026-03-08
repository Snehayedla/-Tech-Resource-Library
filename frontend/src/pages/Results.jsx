import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import ResourceCard from '../components/ResourceCard'
import { getResources } from '../services/api'

function Results() {
  const { technology } = useParams()
  const navigate = useNavigate()
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetchResources()
  }, [technology])

  const fetchResources = async () => {
    try {
      setLoading(true)
      const result = await getResources(technology)
      setData(result)
      setLoading(false)
    } catch (err) {
      if (err.response?.status === 404) {
        setError(`No resources available yet for ${technology}`)
      } else {
        setError('Unable to fetch resources')
      }
      setLoading(false)
    }
  }

  return (
    <div>
      <div className="header">
        <h1>📚 Tech Resource Library</h1>
      </div>

      <div className="container">
        <div className="results-container">
          <button className="back-button" onClick={() => navigate('/')}>
            ← Back to Home
          </button>

          {loading && <div className="loading">Loading resources...</div>}

          {error && <div className="error-message">{error}</div>}

          {!loading && !error && data && (
            <>
              <h1 style={{ marginBottom: '30px', color: '#333' }}>
                {data.technology.name} Resources
              </h1>

              <div className="section">
                <h2>🎥 Top Videos</h2>
                {data.videos.length > 0 ? (
                  <div className="resource-grid">
                    {data.videos.map((video) => (
                      <ResourceCard key={video.id} resource={video} />
                    ))}
                  </div>
                ) : (
                  <p>No videos available</p>
                )}
              </div>

              <div className="section">
                <h2>📝 Top Notes & Tutorials</h2>
                {data.notes.length > 0 ? (
                  <div className="resource-grid">
                    {data.notes.map((note) => (
                      <ResourceCard key={note.id} resource={note} />
                    ))}
                  </div>
                ) : (
                  <p>No notes available</p>
                )}
              </div>

              <div className="section">
                <h2>📖 Top References</h2>
                {data.references.length > 0 ? (
                  <div className="resource-grid">
                    {data.references.map((ref) => (
                      <ResourceCard key={ref.id} resource={ref} />
                    ))}
                  </div>
                ) : (
                  <p>No references available</p>
                )}
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  )
}

export default Results
