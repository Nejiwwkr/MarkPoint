//double slash for comment, and metadata should be written here
theme = 0x8faadc // also ok to use "t = 0x8faadc"

---

//the cover
# The Art of MarkPoint
## Nejiwwkr

---

//contents
# The Maxwell's Equations

## Gauss's Law for Electric Fields

### Integral Form:

$$
\oint_{\partial \mathcal{S}} \mathbf{E} \cdot d\mathbf{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}
$$

### Differential Form:

$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}
$$
//It's fine to use latex formula blocks

## Gauss's Law for Magnetic Fields

### Integral Form:

$$
\oint_{\partial \mathcal{S}} \mathbf{B} \cdot d\mathbf{A} = 0
$$

### Differential Form:

$$
\nabla \cdot \mathbf{B} = 0
$$

// page will be turned at this point, for this page is automatically detected needed to be turned
// the automatically turned page uses the tittle of the last page

## Faraday's Law of Induction

### Integral Form:

$$
\oint_{\partial \mathcal{C}} \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \iint_{\mathcal{S}} \mathbf{B} \cdot d\mathbf{A}
$$

### Differential Form:

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
$$

!!! // also turn page by this way, without detecting the content
// the manually turned page uses the tittle of the last page
//equals: ---\\n#The Maxwell's Equations

Here's the start of the page, feel free to use !!! In the content.

## Ampère's Law with Maxwell's Addition

### Integral Form:

$$
\oint_{\partial \mathcal{C}} \mathbf{B} \cdot d\mathbf{l} = //line break and comment is fine in formula block
\mu_0 I_{\text{enc}} + \mu_0 \varepsilon_0 \frac{d}{dt} \iint_{\mathcal{S}} \mathbf{E} \cdot d\mathbf{A}
$$

### Differential Form:

$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
$$

These equations form the foundation of classical electromagnetism, unify the behavior of electric and magnetic fields, and predict the existence of electromagnetic waves.

\nline break here // ESC is fine

___Bold italic___ and __bold__ _is fine_. And flat styles are fine

---

Empty page
//without tittle

---

//the back cover
# Thanks for reading.
## Rendered by MarkPoint.

---