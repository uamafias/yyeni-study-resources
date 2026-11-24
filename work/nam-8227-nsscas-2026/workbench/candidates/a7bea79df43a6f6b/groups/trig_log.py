"""NSSCAS 8227 approved trig/log finite generators (native version 0.1.4).

This module authors instances and criterion memos, not a free-text/photo grader.
Random selection and attempt/exposure history belong to the provider and app.
Every datum is selected from the approved finite domains in domains/trig_log.json.
"""
from copy import deepcopy
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
from html import escape
import json
import math
from pathlib import Path

RECIPES = ["WB8227-trig-rform-equation", "WB8227-principal-inverse", "WB8227-log-linear-model"]
VERSION = "0.1.4"
_FILE = Path(__file__).resolve().parents[1] / "domains" / "trig_log.json"


def choices():
    """Return portable choice descriptors; capacities distinguish tasks from decisions."""
    return deepcopy(json.loads(_FILE.read_text(encoding="utf-8"))["choices"])


def _fraction(value):
    return Fraction(str(value))


def _tex(value):
    q = _fraction(value)
    if q.denominator == 1:
        return str(q.numerator)
    sign = "-" if q < 0 else ""
    return sign + r"\frac{" + str(abs(q.numerator)) + "}{" + str(q.denominator) + "}"


def _decimal(value):
    """Exact decimal for the terminating quarter/half graph coordinates."""
    q = _fraction(value)
    v = Decimal(q.numerator) / Decimal(q.denominator)
    return format(v, "f").rstrip("0").rstrip(".") if "." in format(v, "f") else format(v, "f")


def _rounded(value, places):
    unit = Decimal(1).scaleb(-places)
    return format(Decimal(str(value)).quantize(unit, rounding=ROUND_HALF_UP), f".{places}f")


def _sf(value, figures=3):
    places = figures - 1 - math.floor(math.log10(abs(value))) if value else 0
    return _rounded(value, places)


def _step(action, reason, result):
    return {"action": action, "reason": reason, "result": result}


def _criterion(recipe, branch, part, cid, achievement, mark_type, **extra):
    return dict(criterion_id=f"{recipe}:{branch}:{part}:{cid}", local_criterion_id=cid,
                marks=1, mark_type=mark_type, achievement=achievement, **extra)


def _part(local_part_id, prompt, answer, steps, criteria, **extra):
    return dict(local_part_id=local_part_id, prompt=prompt, reference_answer=answer,
                worked_steps=steps, criteria=criteria, answer_only_marks=0,
                ambiguity_policy="Pending clarification; never infer an unreadable sign or missing working.", **extra)


def _rform(p):
    rid, bid = RECIPES[0], "degree-cycle"
    a, b, c = (p[k] for k in ("a", "b", "c"))
    n = a*a+b*b
    R = math.sqrt(n)
    rtex = str(math.isqrt(n)) if math.isqrt(n)**2 == n else rf"\sqrt{{{n}}}"
    alpha = math.degrees(math.atan2(b, a))
    beta = math.degrees(math.asin(c/R))
    transformed = sorted(z for j in range(-2, 4) for z in (beta+360*j, 180-beta+360*j)
                         if alpha < z < 360+alpha)
    roots = [z-alpha for z in transformed]
    if len(roots) != 2:
        raise ValueError("Admitted R-form instance must have exactly two interior roots")
    alpha2 = _rounded(alpha, 2)
    roots1 = [_rounded(x, 1) for x in roots]
    expr = rf"{a}\sin\theta+{b}\cos\theta"
    if a == 1:
        expr = expr.replace("1\\sin", "\\sin")
    if b == 1:
        expr = expr.replace("1\\cos", "\\cos")
    ac = [
        _criterion(rid,bid,"a-convert","a-B1",f"Positive exact amplitude $R={rtex}$ in eligible working. An unsimplified non-square surd is accepted; a perfect square must be evaluated.","B"),
        _criterion(rid,bid,"a-convert","a-M1",rf"Visible correct coefficient comparison, $R\cos\alpha={a}$ and $R\sin\alpha={b}$, or equivalent triangle method; $\tan\alpha={b}/{a}$.","M"),
        _criterion(rid,bid,"a-convert","a-A1",rf"Correct acute phase $\alpha={alpha2}^\circ$, or a more precise correct value, with eligible method.","A")]
    bc = [
        _criterion(rid,bid,"b-roots","b-M1",rf"Hence make sine the subject using their positive amplitude and admissible acute phase: $\sin(\theta+\alpha_{{\rm their}})={c}/R_{{\rm their}}$.","M",follow_through=True),
        _criterion(rid,bid,"b-roots","b-M2",r"Complete transformed-root search in their shifted interval $(\alpha_{\rm their},360^\circ+\alpha_{\rm their})$, including explicit rejection of any endpoints. Use their equation, not a memorised canonical quadrant table.","DM",depends_on=[f"{rid}:{bid}:b-roots:b-M1"],follow_through=True),
        _criterion(rid,bid,"b-roots","b-A1",rf"One correct original root, ${roots1[0]}^\circ$ or ${roots1[1]}^\circ$, to one decimal place, with visible hence working. Does not require b-M2.","A",accuracy="canonical except an eligible OD-6 misread"),
        _criterion(rid,bid,"b-roots","b-A2",rf"The other correct original root to one decimal place, with visible hence working. Withhold this award if an extra distinct final value is submitted, including an out-of-interval coterminal value.","A",accuracy="canonical except an eligible OD-6 misread")]
    return {
        "stem": r"Angles are in degrees. Show your working in both parts.",
        "parts": [
            _part("a-convert",rf"Express ${expr}$ as $R\sin(\theta+\alpha)$, where $R>0$ and $0^\circ<\alpha<90^\circ$. Give $R$ exactly and $\alpha$ to two decimal places.",
                  rf"${rtex}\sin(\theta+{alpha2}^\circ)$.",[
                      _step("Expand the requested form.","The sine addition formula gives the coefficients of sine and cosine separately.",rf"$R\sin(\theta+\alpha)=R\cos\alpha\sin\theta+R\sin\alpha\cos\theta$. Thus $R\cos\alpha={a}$ and $R\sin\alpha={b}$.") ,
                      _step("Find the positive amplitude.",r"Squaring and adding uses the identity $\cos^2\alpha+\sin^2\alpha=1$.",rf"$R^2={a}^2+{b}^2={n}$, so $R={rtex}$."),
                      _step("Find the acute phase.","Dividing the coefficient equations fixes the ratio in the required order.",rf"$\tan\alpha=\frac{{{b}}}{{{a}}}$, hence $\alpha={alpha2}^\circ$ to two decimal places.")],ac),
            _part("b-roots",rf"Hence solve ${expr}={c}$ for $0^\circ<\theta<360^\circ$. Give all solutions to one decimal place.",
                  rf"$\theta={roots1[0]}^\circ$ or $\theta={roots1[1]}^\circ$.",[
                      _step("Use the conversion from part (a).","The requested hence method uses the earlier amplitude and phase.",rf"$\sin(\theta+\alpha)=\frac{{{c}}}{{{rtex}}}$, retaining the unrounded values of $R$ and $\alpha$."),
                      _step("Search the full shifted interval.",r"The restriction on the original angle becomes a shifted interval for $z=\theta+\alpha$.",rf"$\alpha<z<360^\circ+\alpha$. The two retained transformed roots are $z\approx{_rounded(transformed[0],6)}^\circ$ and $z\approx{_rounded(transformed[1],6)}^\circ$."),
                      _step("Subtract the phase and check.","Only angles inside the original strict interval solving the original equation are retained.",rf"$\theta=z-\alpha$, giving ${roots1[0]}^\circ$ and ${roots1[1]}^\circ$ to one decimal place.")],bc)
        ],
        "practice_help": {"title":"Keep the coefficient order and the interval", "prompts":["Expand the requested sine form and compare its two coefficients.","After converting, write down the shifted interval before looking for every root.","Keep unrounded values in the calculation and round only the requested answers."]},
        "assets": [],
        "exposure_keys": [f"8227:rform:conversion:{a}:{b}:sin-plus:degrees",f"8227:rform:equation:{a}:{b}:{c}:0-360:hence"],
        "subdecision_exposure_keys": [f"8227:rform:phase-ratio:{Fraction(b,a)}"],
        "private_math": {"R_squared":n,"alpha_degrees":alpha,"roots_degrees":roots,"transformed_roots":transformed},
        "marking_notes": ["Bare correct conversion or bare correct roots earn zero for the respective part under OD-1.","A visible non-hence root method earns zero in part (b); no borrowed special-case award.","Gross dependency awards survive any later MR03-OPS-D4 deduction. Eligible OD-6 misread follow-through does not override OD-1 or MR09.","Use decimal round-half-up. Premature rounding loses only affected accuracy awards."]}


_ANGLE = {"pi/6":Fraction(1,6),"pi/4":Fraction(1,4),"pi/3":Fraction(1,3),
          "2*pi/3":Fraction(2,3),"3*pi/4":Fraction(3,4),"pi":Fraction(1)}


def _angle_fraction(theta):
    return (-1 if theta.startswith("-") else 1)*_ANGLE[theta.lstrip("-")]


def _angle_tex(theta):
    q = _angle_fraction(theta)
    n = abs(q.numerator)
    numer = (str(n) if n != 1 else "") + r"\pi"
    return ("-" if q < 0 else "") + (numer if q.denominator == 1 else rf"\frac{{{numer}}}{{{q.denominator}}}")


def _principal(p):
    rid, bid = RECIPES[1], "solve-or-explain"
    k, theta = p["k"], p["theta"]
    q, tt = _angle_fraction(theta), _angle_tex(theta)
    valid = abs(q) <= Fraction(1,2)
    sign = "-" if q < 0 else ""
    special = {Fraction(1,6):"1",Fraction(1,4):r"\sqrt{2}",Fraction(1,3):r"\sqrt{3}"}
    # All in-range targets are non-axis special angles in this accepted pilot.
    if valid:
        numerator = special[abs(q)]
        exact = sign + (rf"\frac{{1}}{{{2*k}}}" if numerator == "1" else rf"\frac{{{numerator}}}{{{2*k}}}")
        comparison = rf"$-\frac{{\pi}}{{2}}<{tt}<\frac{{\pi}}{{2}}$"
        forward = sign + (r"\frac{1}{2}" if numerator == "1" else rf"\frac{{{numerator}}}{{2}}")
        answer = rf"$x={exact}$."
        steps = [
            _step("Check the actual target.",r"The principal inverse sine takes values only in the closed interval from $-\pi/2$ to $\pi/2$.",comparison + ", so this target is compatible with the principal range."),
            _step("Take sine of both sides.","For an admissible principal target, the inverse relation recovers the argument uniquely.",rf"${k}x=\sin\left({tt}\right)={forward}$."),
            _step("Divide by the nonzero coefficient.","This gives the exact value of the unknown; its argument lies in the sine-inverse domain.",answer)]
    else:
        comparison = rf"${tt}>\frac{{\pi}}{{2}}$" if q>0 else rf"${tt}<-\frac{{\pi}}{{2}}$"
        answer = "There is no real solution."
        steps = [
            _step("Use the principal inverse-sine range.",r"Every real value of an inverse sine is between $-\pi/2$ and $\pi/2$, including the endpoints.",r"$-\frac{\pi}{2}\leq\sin^{-1}(kx)\leq\frac{\pi}{2}$ whenever the inverse is real."),
            _step("Compare this question's target with that range.","The target has to be an actual value of the principal inverse, not merely have the same forward sine.",comparison + ", outside the principal range."),
            _step("State the consequence.","An out-of-range target cannot be the value of a real principal inverse sine.",answer)]
    criteria = [
        _criterion(rid,bid,"p-decision","P-B1",f"Apply the principal inverse property to the actual target {comparison}, or verify/reject a forced candidate by its actual principal inverse. A rote interval statement alone is insufficient.","B"),
        _criterion(rid,bid,"p-decision","P-M1",rf"For a real target, show ${k}x=\sin({tt})$ (a correct decimal intermediate is allowed). For an out-of-range target, show the applied range obstruction or a complete forced-candidate contradiction.","M"),
        _criterion(rid,bid,"p-decision","P-A1",f"{answer} Supported by eligible reasoning; a real-case final value must be exact. An arbitrary failed guess is not a no-solution proof.","A")]
    return {"stem":"All angles are in radians. Show your working.",
            "parts":[_part("p-decision",rf"Solve $\sin^{{-1}}({k}x)={tt}$, giving an exact solution, or explain why it has no real solution.",answer,steps,criteria)],
            "practice_help":{"title":"Check the inverse relation", "prompts":["What values can a principal inverse sine take? Apply that fact to the given target.","If you take sine, check the resulting candidate in the original inverse equation.","Keep exact values until the final answer."]},
            "assets":[],"exposure_keys":[f"8227:principal:inverse-sine:{theta}:neutral-contract"],
            "private_math":{"outcome":"real-solution" if valid else "no-real-solution","theta_pi_coefficient":str(q),"exact_solution":exact if valid else None},
            "conditional_direct_demand_ids":["8227:2020:M1:T6:O03:D01"] if valid else [],
            "conditional_direct_objective_ids":["8227:2020:M1:T6:O03"] if valid else [],
            "conditional_metadata_visibility":"private until submission: resolved exact-angle tags would reveal the outcome",
            "marking_notes":["This unified task is syllabus-derived; the comparable Cambridge algebra facet is related, not a same-type label for the whole task.","Bare correct value or unexplained no-real conclusion earns zero. Actual-target property plus forward recovery are distinct evidence slots.","A valid forced-candidate contradiction is an accepted full-credit alternative without a separately written interval.","Designed no-real outcomes can retain OD-6 eligibility when object/difficulty are preserved; flipping real/no-real is ineligible."]}


def _rect_segment(rect, a, b):
    """Closed rectangle/segment intersection (Liang-Barsky), for label safety."""
    x0,y0,x1,y1=rect; ax,ay=a; bx,by=b
    lo,hi=0.0,1.0
    for p,q in [(-(bx-ax),ax-x0),(bx-ax,x1-ax),(-(by-ay),ay-y0),(by-ay,y1-ay)]:
        if abs(p)<1e-12:
            if q<0:return False
        elif p<0:
            lo=max(lo,q/p)
        else:hi=min(hi,q/p)
        if lo>hi:return False
    return True


def _overlap(a,b):
    return not(a[2]<b[0] or b[2]<a[0] or a[3]<b[1] or b[3]<a[1])


def _graph_svg(L,p,x1,dx):
    """Exact labels with checked transparent placements; all 270 are exercised by author checks."""
    x2=x1+dx; u1=p*x1+p+L;u2=p*x2+p+L
    width,height=1200,640
    left,right,top,bottom=95,1100,55,550
    xmin,xmax=-0.7,float(x2)+1.2
    edge=[float(p)*xmin+float(p+L),float(p)*xmax+float(p+L),float(u1),float(u2),0.0]
    ymin,ymax=min(edge)-1.8,max(edge)+1.8
    X=lambda x:left+(float(x)-xmin)/(xmax-xmin)*(right-left)
    Y=lambda u:bottom-(float(u)-ymin)/(ymax-ymin)*(bottom-top)
    a=(X(xmin),Y(float(p)*xmin+float(p+L)));b=(X(xmax),Y(float(p)*xmax+float(p+L)))
    origin=(X(0),Y(0)); axes=[((left,origin[1]),(right,origin[1])),((origin[0],top),(origin[0],bottom))]
    coords=[(x1,u1),(x2,u2)]
    placements=[]
    # Centre-to-baseline candidates; conservative 17px character boxes cover the 28px font.
    for x,u in coords:
        label=f"({x}, {_decimal(u)})"; px,py=X(x),Y(u); tw=17*len(label)+8
        chosen=None
        for oy in [-52,42,-88,78,-124,114,-160,150]:
            for ox in [24,-tw-24,45,-tw-45,90,-tw-90]:
                tx,ty=px+ox,py+oy;box=(tx-4,ty-30,tx+tw,ty+9)
                if box[0]<left+4 or box[2]>right-4 or box[1]<top+3 or box[3]>bottom-4:continue
                if _rect_segment(box,a,b) or any(_rect_segment(box,*s)for s in axes):continue
                if any(_overlap(box,t['box'])for t in placements):continue
                if any(box[0]-6<X(xx)<box[2]+6 and box[1]-6<Y(uu)<box[3]+6 for xx,uu in coords):continue
                chosen=dict(text=label,x=tx,y=ty,box=box,point=(px,py));break
            if chosen:break
        if chosen is None:raise ValueError("No safe graph coordinate-label placement")
        placements.append(chosen)
    lines=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="640" viewBox="0 0 1200 640" role="img" aria-labelledby="title desc">',
           '<title id="title">Straight-line graph of ln y against x</title>',
           '<desc id="desc">'+escape(f'Horizontal axis x; vertical axis ln y. Exact coordinates {placements[0]["text"]} and {placements[1]["text"]}. The labelled points are on one straight line. Schematic; use labels, not measurements.')+'</desc>',
           '<rect width="1200" height="640" fill="white"/>',
           '<g stroke="#202020" stroke-width="2" fill="none">']
    for aa,bb in axes:lines.append(f'<line x1="{aa[0]:.4f}" y1="{aa[1]:.4f}" x2="{bb[0]:.4f}" y2="{bb[1]:.4f}"/>')
    lines.extend(['</g>',f'<line x1="{a[0]:.4f}" y1="{a[1]:.4f}" x2="{b[0]:.4f}" y2="{b[1]:.4f}" stroke="#174777" stroke-width="3"/>',
                  f'<g font-family="Arial, sans-serif" font-size="28" fill="#111"><text x="{right+20}" y="{origin[1]+7:.4f}">x</text><text x="{origin[0]-22:.4f}" y="{top-16}">ln y</text><text x="{origin[0]-24:.4f}" y="{origin[1]+29:.4f}">0</text>'])
    for t in placements:
        px,py=t['point'];lines.extend([f'<circle cx="{px:.4f}" cy="{py:.4f}" r="5" fill="#174777"/>',f'<text x="{t["x"]:.4f}" y="{t["y"]:.4f}">{escape(t["text"])}</text>'])
    lines.extend(['<text x="95" y="605" font-size="18">Schematic graph. Use the exact labelled coordinates, not measurements.</text>','</g></svg>'])
    return '\n'.join(lines)+'\n', dict(label_boxes=[t['box']for t in placements],labels=[t['text']for t in placements],line_segment=[a,b],axes=axes,viewport=[width,height],exact_points=[[str(x),str(u)]for x,u in coords])


def _graph(p):
    rid,bid=RECIPES[2],"graph-intercept"
    L,pp=_fraction(p["L"]),_fraction(p["p"]);x1,dx=p["x1"],p["delta_x"];x2=x1+dx
    u1=pp*x1+pp+L;u2=pp*x2+pp+L
    A=math.exp(float(L));atex=rf"e^{{{_tex(L)}}}"
    svg,layout=_graph_svg(L,pp,x1,dx)
    criteria=[
        _criterion(rid,bid,"g-parameters","G-B1",r"Correct transformed line $\ln y=px+p+\ln A$, stated or implied by visible coordinate equations. Bare final parameters do not imply it.","B"),
        _criterion(rid,bid,"g-parameters","G-M1","Identify p with the gradient and attempt the gradient from the two exact coordinates; a valid simultaneous-equation method occupies the same award.","M"),
        _criterion(rid,bid,"g-parameters","G-A1",rf"Correct $p={_tex(pp)}$ with eligible working.","A"),
        _criterion(rid,bid,"g-parameters","G-M2",r"Coherent substitution of a coordinate and simplification to $A=e^{\text{constant}}$. An earlier coherent transformed-line/parameter slip can follow through; do not require the correct +p solely for this method award.","DM",depends_on=[f"{rid}:{bid}:g-parameters:G-M1"],follow_through=True),
        _criterion(rid,bid,"g-parameters","G-A2",rf"Correct $A={atex}$ or ${_sf(A)}$ to three significant figures, with eligible working. The coupled +p is needed for canonical accuracy.","A")]
    steps=[
        _step("Take natural logarithms.","Apply the product and exponent laws before comparing with a line.",r"$\ln y=px+p+\ln A$."),
        _step("Read the exact coordinates and calculate the gradient.","The horizontal variable is x and the vertical variable is ln y, so the slope is p.",rf"$p=\frac{{{_decimal(u2)}-({_decimal(u1)})}}{{{x2}-{x1}}}={_tex(pp)}$."),
        _step("Substitute one point into the complete transformed equation.","Both p terms are part of the supplied model; the intercept is p + ln A.",rf"${_decimal(u1)}={x1}\left({_tex(pp)}\right)+\left({_tex(pp)}\right)+\ln A$, hence $\ln A={_tex(L)}$."),
        _step("Recover the amplitude.","The exponential function undoes the natural logarithm; A must be positive.",rf"$A={atex}\approx{_sf(A)}$, with $p={_tex(pp)}$.")]
    return {"stem":r"The variables satisfy $y=Ae^{px+p}$, where $A>0$. The graph of $\ln y$ against $x$ is shown. Use its exact labelled coordinates; the drawing is schematic.",
            "parts":[_part("g-parameters","Find $A$ and $p$, giving any non-exact decimal answers to three significant figures. Show your working.",rf"$A={atex}\approx{_sf(A)}$ and $p={_tex(pp)}$.",steps,criteria)],
            "assets":[dict(asset_id="log-line",role="question",svg=svg,alt="Graph of ln y against x through exact coordinates "+", ".join(layout['labels'])+". Schematic; use labels, not measurements.",must_read_givens=["horizontal axis x","vertical axis ln y","both exact coordinate labels","the points lie on the same straight line"],diagram_parameters={"fixed":["Cartesian axes","ln y vertical axis","schematic; no measuring"],"variable":{"points":layout['exact_points']},"relations":["u_i=p*x_i+p+ln(A)","x2>x1","all exact labels remain visible"]},layout_checks=layout)],
            "practice_help":{"title":"Read the transformed line", "prompts":["Write the supplied model using the logarithm shown on the vertical axis.","Which coefficient is the gradient, and what is contained in the intercept?","Use one exact labelled coordinate to recover the remaining constant."]},
            "exposure_keys":[f"8227:log:coupled-model:{L}:{pp}:lny-x"],
            "private_math":{"L":str(L),"p":str(pp),"A":A,"exact_points":layout['exact_points']},
            "marking_notes":["Correct simultaneous coordinate equations can imply the log-line; both methods share the five-mark cap.","A coherent missing-offset line can retain gradient and dependent substitution method credit (3/5 when those are the only earned awards).", "Bare final parameters earn zero. An opaque label box must never cover the line; layout coordinates are authoring evidence, not learner answers."]}


def _gradient(p):
    rid,bid=RECIPES[2],"gradient-target"
    b,c,m,q=(p[k]for k in ('b','c','m','q'));a=b**m;x=Fraction(q-c*a,m)
    pref= "a" if c==1 else f"{c}a"
    model=rf"y={b}^{{{pref}}}a^x"; target="1" if q==0 else str(b) if q==1 else rf"{b}^{{{q}}}"
    ac=[
        _criterion(rid,bid,"t-parameter","T-B1",rf"Correct transformed line $\log_{{{b}}}y={pref}+x\log_{{{b}}}a$, stated or implied by visible work. Equivalent ln/lg transformations are accepted with the plotted-base gradient mapped correctly.","B"),
        _criterion(rid,bid,"t-parameter","T-M1",rf"State or imply $\log_{{{b}}}a={m}$, or the equivalent $\ln a/\ln {b}={m}$, from the actual plotted gradient.","M"),
        _criterion(rid,bid,"t-parameter","T-A1",rf"Correct exact value $a={a}$ with eligible method.","A")]
    bc=[
        _criterion(rid,bid,"t-target","U-M1",rf"Hence use their positive $a\ne1$ and this target in their earlier log equation, a correct log equation first written here, or the original/exponent equation. Consistent substitution into an earlier missing-prefactor line follows through; newly dropping a previously retained prefactor does not earn this award.","M",follow_through=True),
        _criterion(rid,bid,"t-target","U-A1",rf"Correct $x={_tex(x)}$, exact or correctly rounded to three significant figures, with eligible hence working.","A",accuracy="canonical except an eligible OD-6 misread")]
    answer=rf"$x={_tex(x)}$"+(rf" $\approx{_sf(float(x))}$" if x.denominator!=1 else "")+"."
    return {"stem":rf"The model is ${model}$, where $a$ is positive. A graph of $\log_{{{b}}}y$ against $x$ has gradient ${m}$. Show your working.",
            "parts":[
                _part("t-parameter","Find $a$ exactly.",rf"$a={a}$.",[
                    _step("Take logarithms to the plotted base.","The product and exponent laws express the ordinate as a straight-line function of x.",rf"$\log_{{{b}}}y={pref}+x\log_{{{b}}}a$."),
                    _step("Match the gradient and exponentiate.","The coefficient of x is the given gradient.",rf"$\log_{{{b}}}a={m}$, hence $a={b}^{{{m}}}={a}$.")],ac),
                _part("t-target",rf"Hence find $x$ when $y={target}$. Give an exact answer or a decimal correct to three significant figures.",answer,[
                    _step("Substitute the recovered parameter and the target.","The hence method uses the result from part (a) in the same model.",rf"${q}={c*a}+{m}x$."),
                    _step("Solve the resulting linear equation.","Subtract the constant term and divide by the nonzero gradient.",rf"$x=\frac{{{q}-{c*a}}}{{{m}}}={_tex(x)}$."),
                    _step("Check in the original exponential model.","Rewriting all powers to the supplied base checks the target without large decimal calculations.",rf"${b}^{{{c*a}}}\left({b}^{{{m}}}\right)^{{{_tex(x)}}}={b}^{{{c*a}+{m}\left({_tex(x)}\right)}}={b}^{{{q}}}$.")],bc)
            ],"assets":[],
            "practice_help":{"title":"Match the plotted logarithm", "prompts":["Transform using the logarithm base stated for the plotted ordinate.","Match the coefficient of x to the given gradient, then undo that logarithm.","For the hence part, reuse the parameter you found and retain the whole prefactor."]},
            "exposure_keys":[f"8227:log:gradient-model:{b}:{c}:{m}",f"8227:log:target:{b}:{c}:{m}:{q}:hence"],
            "subdecision_exposure_keys":[f"8227:log:exponentiation:{b}:{m}"],
            "private_math":{"a":a,"x":str(x),"target_exponent":q,"log_line_intercept":c*a},
            "marking_notes":["Correct ln/lg routes are alternatives when the gradient is converted to the plotted base; this is not an additional required change-of-base objective.","A visible non-hence method has no borrowed special-case award. Bare answers earn zero per part.","A newly dropped prefactor is distinct from consistent follow-through from an earlier missing-prefactor equation.","Primary parameter-model exposure repeats when only q changes. Version changes do not reset exposure."]}


def build(recipe_id, branch_id, parameters):
    descriptors=[c for c in choices() if c['recipe_id']==recipe_id and c['branch_id']==branch_id]
    if len(descriptors)!=1 or parameters not in descriptors[0]['parameters']:
        raise ValueError("Unknown choice or parameters outside its approved finite domain")
    if recipe_id==RECIPES[0]:return _rform(parameters)
    if recipe_id==RECIPES[1]:return _principal(parameters)
    if branch_id=='graph-intercept':return _graph(parameters)
    return _gradient(parameters)
