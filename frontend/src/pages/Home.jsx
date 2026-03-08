import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import SearchBar from '../components/SearchBar'
import { getTechnologies } from '../services/api'

function Home() {
  const [technologies, setTechnologies] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    fetchTechnologies()
  }, [])

  const fetchTechnologies = async () => {
    try {
      const data = await getTechnologies()
      setTechnologies(data)
      setLoading(false)
    } catch (err) {
      setError('Unable to fetch technologies')
      setLoading(false)
    }
  }

  const handleTechClick = (techName) => {
    navigate(`/results/${techName}`)
  }

  return (
    <div>
      <div className="header">
        <h1>📚 Tech Resource Library</h1>
        <p>Find the best learning resources for any technology</p>
        <p>This project is created for learning and skill development purposes. The resources, videos, and materials referenced belong to their respective creators and are shared only to help learners easily discover useful content in one place. I do not claim ownership of these resources. The goal of this project is to simplify access to learning materials and practice building real-world web applications. </p>
      </div>

      <div className="container">
        <SearchBar />

        {loading && <div className="loading">Loading technologies...</div>}
        
        {error && <div className="error-message">{error}</div>}

        {!loading && !error && (
          <div className="tech-list">
            {technologies.map((tech) => (
              <div
                key={tech.id}
                className="tech-card"
                onClick={() => handleTechClick(tech.name)}
              >
                <h3>{tech.name}</h3>
                <p>{tech.description}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

export default Home
