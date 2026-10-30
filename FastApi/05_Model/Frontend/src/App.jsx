import { useState } from 'react'

const OCCUPATIONS = [
  ['private_job', 'Private job'],
  ['government_job', 'Government job'],
  ['business_owner', 'Business owner'],
  ['freelancer', 'Freelancer'],
  ['student', 'Student'],
  ['retired', 'Retired'],
  ['unemployed', 'Unemployed'],
]

const initial = {
  age: '',
  weight: '',
  height: '',
  income_lpa: '',
  smoker: false,
  city: '',
  occupation: 'private_job',
}

export default function App() {
  const [form, setForm] = useState(initial)
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState('')

  const set = (key) => (e) => {
    const value = e.target.type === 'checkbox' ? e.target.checked : e.target.value
    setForm((f) => ({ ...f, [key]: value }))
  }

  const bmi =
    form.weight && form.height && Number(form.height) > 0
      ? (Number(form.weight) / Number(form.height) ** 2).toFixed(1)
      : null

  const submit = async (e) => {
    e.preventDefault()
    setError('')
    setResult(null)
    setLoading(true)

    const payload = {
      age: parseInt(form.age, 10),
      weight: parseFloat(form.weight),
      height: parseFloat(form.height),
      income_lpa: parseInt(form.income_lpa, 10),
      smoker: form.smoker,
      city: form.city.trim(),
      occupation: form.occupation,
    }

    try {
      const res = await fetch('/api/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })
      const data = await res.json()
      if (!res.ok) {
        // FastAPI validation errors come back as { detail: [{loc, msg}, ...] }
        if (Array.isArray(data.detail)) {
          throw new Error(
            data.detail.map((d) => `${d.loc.slice(-1)[0]}: ${d.msg}`).join(' | ')
          )
        }
        throw new Error(data.detail || 'Something went wrong')
      }
      setResult(data.predicted_category)
    } catch (err) {
      setError(
        err instanceof TypeError
          ? "Can't reach the backend. Is FastAPI running on port 8000?"
          : err.message
      )
    } finally {
      setLoading(false)
    }
  }

  const reset = () => {
    setForm(initial)
    setResult(null)
    setError('')
  }

  return (
    <div className="page">
      <form className="card" onSubmit={submit}>
        <h1>Insurance Premium Predictor</h1>
        <p className="sub">Fill in your details to get a premium category.</p>

        <div className="grid">
          <label>
            Age
            <input type="number" min="1" max="99" required value={form.age} onChange={set('age')} />
          </label>

          <label>
            Income (LPA)
            <input type="number" min="1" required value={form.income_lpa} onChange={set('income_lpa')} />
          </label>

          <label>
            Weight (kg)
            <input type="number" step="0.1" min="1" max="119" required value={form.weight} onChange={set('weight')} />
          </label>

          <label>
            Height (m)
            <input type="number" step="0.01" min="0.5" max="2.49" placeholder="e.g. 1.72" required value={form.height} onChange={set('height')} />
          </label>

          <label>
            City
            <input type="text" placeholder="e.g. Noida" required value={form.city} onChange={set('city')} />
          </label>

          <label>
            Occupation
            <select value={form.occupation} onChange={set('occupation')}>
              {OCCUPATIONS.map(([v, l]) => (
                <option key={v} value={v}>{l}</option>
              ))}
            </select>
          </label>
        </div>

        <label className="check">
          <input type="checkbox" checked={form.smoker} onChange={set('smoker')} />
          I smoke
        </label>

        {bmi && <p className="bmi">BMI: <b>{bmi}</b></p>}

        <div className="actions">
          <button type="submit" disabled={loading}>
            {loading ? 'Predicting...' : 'Predict premium'}
          </button>
          <button type="button" className="ghost" onClick={reset}>Reset</button>
        </div>

        {error && <div className="error">{error}</div>}

        {result && (
          <div className="result">
            <span>Predicted category</span>
            <strong>{result}</strong>
          </div>
        )}
      </form>
    </div>
  )
}
