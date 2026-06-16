# 🔬 Theme 3: Experimental Design & Statistical Inference (A/B Testing)

## 🏢 Executive Overview
If an analytics dashboard shows that sales went up by 15% after a price adjustment, a novice analyst celebrates. A professional analyst asks: *Is this increase statistically significant, or was it just a random seasonal fluke?* This module details how to design, run, and evaluate business experiments with total scientific certainty.

---

## 🔍 Deep-Dive Project Breakdowns

### 1. Retention Economics: Testing Financial Incentive Frameworks
*   **The Academic Source:** `Datos_Banca_ANOVA.xlsx` / `.omv`
*   **The Business Problem:** A financial institution wants to launch a new card acquisition push. They have three competing ideas: a "Cashback" mechanism, a "Zero Commission" model, or a "Travel Points" tier. They need to know which tool drives real performance.
*   **The Solution Engine (Analysis of Variance - ANOVA):**
    *   Instead of looking at simple averages that could be distorted by extreme outliers, we run a formal **ANOVA model**.
    *   The system evaluates the internal variation *within* each promotional group against the variation *across* the groups, computing an explicit $p$-value.
*   **The Strategic Decision:** If our $p$-value falls below our alpha limit ($p < 0.05$), we reject the baseline assumption that all promotions perform equally. We then deploy post-hoc tests to isolate the single champion program, ensuring corporate acquisition budgets are backed by verifiable mathematical proof.

### 2. Pricing Architecture: Elasticity and Markdown Testing
*   **The Academic Source:** `Datos_Estrategias_Precios.xlsx` / `.omv`
*   **The Business Problem:** An e-commerce brand wants to implement aggressive pricing reductions to clear seasonal stock, but fears destroying its long-term baseline margin structure.
*   **The Solution Engine:** 
    *   We run controlled pricing experiments across isolated user cohorts, logging conversion changes against specific discount buckets.
    *   Using statistical inference, we verify whether the volume lift from a markdown yields deep, sustainable revenue shifts, or if the customer pool would have purchased anyway at standard pricing levels.
*   **The Strategic Decision:** The data defines the exact threshold where demand breaks. This prevents the business from running unnecessary discounts, preserving profit margins while liquidating inventory efficiently.
