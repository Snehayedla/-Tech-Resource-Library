import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

function SearchBar() {
  const [searchTerm, setSearchTerm] = useState('')
  const navigate = useNavigate()

  const handleSearch = (e) => {
    e.preventDefault()
    if (searchTerm.trim()) {
      navigate(`/results/${searchTerm.trim()}`)
    }
  }

  return (
    <div className="search-container">
      <form onSubmit={handleSearch} className="search-box">
        <input
          type="text"
          placeholder="Search for a technology (e.g., Python, React, Java)..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <button type="submit">Search</button>
      </form>
    </div>
  )
}

export default SearchBar
