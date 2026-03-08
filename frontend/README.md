# Frontend - Tech Resource Library

React frontend for the Tech Resource Library application.

## Structure

```
frontend/
├── src/
│   ├── components/      # Reusable components
│   │   ├── SearchBar.jsx
│   │   └── ResourceCard.jsx
│   ├── pages/           # Page components
│   │   ├── Home.jsx
│   │   └── Results.jsx
│   ├── services/        # API integration
│   │   └── api.js
│   ├── App.jsx          # Main app with routing
│   ├── main.jsx         # React entry point
│   └── index.css        # Global styles
├── index.html           # HTML template
├── package.json         # Dependencies
└── vite.config.js       # Vite configuration
```

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start development server:
   ```bash
   npm run dev
   ```

3. Build for production:
   ```bash
   npm run build
   ```

## Components

### SearchBar
Search input component with auto-suggestions.

### ResourceCard
Displays individual resource with title, URL, and views.

## Pages

### Home
Landing page with search functionality and technology cards.

### Results
Displays categorized resources (videos, notes, references) for selected technology.

## API Integration

All API calls are centralized in `src/services/api.js`:
- `getTechnologies()` - Fetch all technologies
- `getResources(technology)` - Fetch resources for a technology
- `createResource(data)` - Add new resource
- `deleteResource(id)` - Delete resource

## Styling

The application uses vanilla CSS for styling. Global styles are in `index.css`.

## Adding New Components

1. Create component file in `src/components/`
2. Import and use in pages
3. Keep components small and focused

## Environment

The API base URL is configured in `src/services/api.js`:
```javascript
const API_BASE_URL = 'http://localhost:8000'
```
