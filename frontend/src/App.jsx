import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import Home from './pages/Home'
import Classifier from './pages/Classifier'
import About from './pages/About'
import VegetablesShowcase from './pages/VegetablesShowcase'
import './App.css'
import './styles/ninjacart.css'

function App() {
  return (
    <Router>
      <div className="app-wrapper">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/vegetables" element={<VegetablesShowcase />} />
          <Route path="/classifier" element={<Classifier />} />
          <Route path="/about" element={<About />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  )
}

export default App
