# Three-Point Estimator Toolkit  
*Modular. Strategic. Reusable.*

> 🖥️ Live Dashboard: [View on AWS S3](http://estimationdashboard.s3-website-us-east-1.amazonaws.com)  
> 🔗 HTML Prototype: [View on S3](http://threepointestimator.s3-website-us-east-1.amazonaws.com)  
> 📊 API Docs (Swagger): [https://three-point-api.onrender.com/apidocs/](https://three-point-api.onrender.com/apidocs/)

---

## ✨ Overview

This toolkit reimagines how estimation can support both strategic planning and operational excellence.

It includes:
- 🔧 A reusable Python API (Flask)
- 📈 An interactive React estimation dashboard
- 📝 A strategic BRD with HTML wireframe and prototype
- 📊 A product management white paper
- 🧠 A case study on estimation ROI

This isn't just an app—it's a product-thinking artifact built to show how strategy, planning, and execution connect.

---

## 🚀 Architecture Highlights

| Layer        | Tool/Tech         | Purpose                            |
|--------------|-------------------|------------------------------------|
| Frontend     | HTML + React      | Dashboard for data input & output |
| API Backend  | Flask + Flasgger  | Lightweight reusable service       |
| Deployment   | S3 + Render       | Cloud hosting (public)             |
| Export       | jsPDF + Blob CSV  | Download TE results + snapshots    |

---

## 🧩 Use Cases & Reusability

This tool can be used by:
- Strategic planners to pre-capture sizing estimates
- QA leads for cycle planning
- Agile teams for What-If capacity simulations
- PMs integrating into JIRA, dashboards, or SAFe comparisons

The Flask API can be:
- Embedded into engineering workflows
- Queried from product enablement scripts
- Extended to integrate with JIRA, ServiceNow, or Datadog

---

## 📁 Repo Structure

```
/docs/
├── Whitepaper.pdf
├── Case Study.pdf
├── Playbook.pdf
├── QA Test Strategy.pdf
├── SAFe vs 3 Point Commentary.pdf
├── Lifecycle Roadmap.pdf
├── BRD - Estimation Tool.docx
├── index.html  ← (GitHub Pages redirect)
/api/
├── app.py
├── requirements.txt
/tool/
├── threepointestimator.html
/images/
├── dashboard.png
├── html-prototype.png
├── swagger.png
```

---

## 💡 Why This Matters

Estimation isn’t just a numbers game—it’s a lens into how teams think, plan, and prioritize.

This tool creates a flexible, clear, and confidence-building framework for estimating effort, aligning resources, and scaling delivery maturity. It’s easy to implement, but designed to spark strategic clarity and continuous improvement.

---

## 🧠 What This Shows About Me

This project reflects how I lead—with a bias for clarity, reusability, and transformation.

It demonstrates:
- Strategic systems thinking (top-down and bottom-up)
- Full-stack implementation (from white paper to API)
- Business and technical fluency
- Product mindset anchored in usability and adaptability

It’s not just code—it’s a reflection of how I pivot with power, on purpose.

---

## 🛠️ How to Run Locally

```bash
# Run the Flask API
cd api
pip install -r requirements.txt
python app.py

# Start the React dashboard (if applicable)
cd dashboard/estimation-dashboard-react
npm install
npm start
```

Or simply open the HTML tool:
```
/tool/threepointestimator.html
```

---

<sub>© 2025  Donell Adams-Welch. Reuse by permission only.</sub>
