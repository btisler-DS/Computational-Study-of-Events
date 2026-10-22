# From Interaction to Observation

## A Computational Study of Events, Questions, and Information Formation

**Bruce Tisler**  
Quantum Inquiry  
**Working manuscript v0.1.0 · October 2026**

This is a versioned text edition of the working manuscript. Its experimental observations are distinguished from the interpretive proposal. Figures are preserved in the author’s illustrated PDF and are intended for separate deposition in this repository.

---

## Abstract
When two objects interact, the interaction can produce something that did not previously exist.
That result carries a history of its origin and can participate in subsequent interactions, producing
further changes over time. This simple relationship provides the foundation for an investigation
into how information emerges, develops, and becomes available to an observer.

We constructed a series of reproducible computational experiments beginning with two moving
objects, A and B, inside a bounded environment. The experiments follow five basic rules:
## 1. Objects move continuously within the boundary and reflect when they encounter its
      walls.
## 2. When two objects collide, their trajectories change and a new, smaller object, c, is
      generated.
## 3. When a smaller object subsequently collides with another object, it grows to normal size.
      That collision can also generate another small object.
## 4. Every generated object continues moving and can participate in further collisions,
      allowing the process to repeat.
## 5. Observers move within the same environment and can encounter the original c. Their
      encounters are recorded with the time, location, state, and history of c, without changing
      its motion or causing its growth.

The experiments progressively extend these rules from two-dimensional motion to a three-
dimensional environment containing three observers. Persistent and fading colored trajectories
allow the developing system and its history to be viewed simultaneously.

To understand the significance of multiple observers, consider a traffic accident. Two vehicles
collide, producing an event with consequences and a history. A bystander witnesses the accident,
a traffic officer investigates what happened, and an insurance adjuster examines the resulting
damage. All three encounter the same occurrence, yet each may ask different questions and form
a different understanding of what happened. The accident and its history remain the same while
the information formed by each observer differs.

This relationship raises a broader question about the nature of information and observation. An
event can occur and develop independently of anyone observing it. When an observer encounters
that event, the questions they ask may determine which aspects of its history become meaningful
to them. Different observers can therefore develop distinct understandings from the same
originating event.

The investigation explores whether this process offers a way to visualize and understand how
information is formed and how that information contributes to what an observer recognizes as a
form of reality.

The paper presents the experimental methods, recorded results, and examples that motivated this
interpretation, allowing readers to examine the progression from interaction to observation and
independently evaluate the proposed relationship between questions, information, and reality.
## 1. Introduction: From Interaction to Observation
Consider two objects moving through space. Each has a position, direction, and history of
movement. At some point, their paths intersect and they collide. The interaction changes their
motion and establishes an event that can be described by what occurred, where it occurred, when
it occurred, and what followed.

Now imagine a simple computer simulation in which that collision also generates a third, smaller
object. The new object moves independently, encounters other objects, and participates in further
interactions. As the process continues, additional objects emerge, each with a history that can be
traced to the interaction that produced it.

This is the starting point of our investigation.

We identify the two original objects as A and B, and the resulting smaller object as c. Their
relationship is expressed as:


$$
A+B\rightarrow c
$$

The notation describes a simple sequence: two objects interact, and their interaction produces a
result. The complete event includes A, B, their interaction, and the resulting c.

Once c exists, it becomes part of the environment in which subsequent events occur. It can
occupy the role of A or B in another interaction, producing another c. The process can continue,
with each new interaction changing the conditions under which later interactions take place.

Over time, the simulation develops a population of moving objects. Their trajectories cross,
collisions occur at different locations, and the history becomes increasingly complex. Yet each
generated object can be traced to an originating interaction. What initially appears to be an
irregular collection of movements is also a record of events unfolding through time.

This brings us to observation.

Imagine entering the simulation after it has been running. You encounter one of the generated
objects. You can observe its present location, size, and direction of movement. If the simulation
retains its history, you can also discover when the object emerged, which objects participated in
its creation, and what interactions occurred afterward.

You are examining an event that began before your observation.

Another observer may encounter the same object at a different time or location. That observer
has access to the same underlying history, although the information available during the
encounter may differ. Each observer may become interested in different aspects of what
occurred.

One observer might ask where the object came from. Another might ask how it reached its
present position. A third might ask what happens when it interacts with another object.

Each question directs attention toward a particular relationship within the history of the same
object.

The significance of this progression becomes clearer when we consider ordinary events. A traffic
accident, for example, may be witnessed by a bystander, investigated by a traffic officer, and
evaluated by an insurance adjuster. The collision is a shared occurrence with a particular history.
The questions each person asks determine which aspects of that history become the subject of
inquiry.

Our computational experiment provides a way to examine these relationships visually. We can
observe the original interaction, follow the resulting objects through subsequent events, and
introduce observers whose encounters with the same object are recorded independently.

The investigation begins with these observable relationships: an event occurs, a result emerges, a
history develops, and observers encounter that history.

From this foundation, we can examine how information becomes available through observation,
how questions direct attention toward particular relationships, and how different understandings
may arise from the same originating event.
## 2. Experimental Design and Methods
### 2.1 Building the environment
The experiment was designed to make the consequences of repeated interactions visible over
time. We began with a square containing two moving balls. The square establishes a boundary,
and the balls represent objects capable of movement and interaction.

Each ball has a position, a direction of movement, and a speed. When a ball reaches a wall, it
reflects and continues moving within the square. When two balls collide, their directions of
motion change according to the collision calculations.

The simulation follows the movement of every ball, recording its position and interactions as
time progresses.

The first two balls are identified as A and B. We assign green to A and blue to B so that their
individual trajectories remain distinguishable throughout the experiment.

The simulation begins with these two objects alone.
### 2.2 Introducing the generation rule
The first additional rule concerns what happens when two balls collide.

In an ordinary billiard simulation, the balls would change direction and continue moving. We
added one condition: a qualifying collision also generates a new, smaller ball.

When A and B first collide, this new ball is identified as c and colored red.

The relationship is:


$$
A+B\rightarrow c
$$

The new ball begins moving independently. It has its own position, direction, and speed. The
simulation also records the collision that produced it.

A and B continue moving after the collision, while c becomes a third participant in the
environment.

The creation of c changes the system. Before the collision, there were two moving objects.
Afterward, there are three, each capable of further interactions.

The simulation now has more possible encounters than it did at the beginning.
### 2.3 Allowing the process to repeat
The generation rule applies to subsequent collisions.

When any two ordinary balls undergo a qualifying collision, the simulation attempts to generate
another small ball. This includes collisions involving balls produced by earlier interactions.

Consider the following sequence.

A and B collide, producing c. As c moves through the environment, it may later collide with A,
B, or another generated ball. That interaction changes the participants' motion and can produce
another small ball.

The newly generated ball is also free to participate in future collisions.

Each generation therefore contributes additional moving objects to the same environment. These
objects can become participants in later events, allowing the process to continue.

The labels A and B describe the roles occupied by the two objects participating in an interaction.
They are also the permanent identifiers of the original green and blue balls. A generated c can
occupy either participating role in a later interaction while retaining its own individual identity
and recorded origin.

This allows us to distinguish the object's history from its current role in the system.
### 2.4 Representing changes of state
We introduced a visible difference between a newly generated ball and one that has participated
in a subsequent collision.

A newly generated ball begins smaller than the original objects and is colored red.

When a small ball participates in a qualifying collision with another ordinary ball, it grows to
normal size. Its current color changes to yellow. That collision can also generate another small
red ball.

The color change allows the viewer to identify an object that has undergone this transition.

The simulation preserves the original object's identity and history throughout its movement and
growth. Its recorded origin remains associated with the interaction that first produced it.

These rules allow us to observe three related developments: the appearance of new objects, their
subsequent interactions, and their changes of state.

The original A and B remain green and blue. Their colors continue to identify the starting
conditions.
### 2.5 Making the history visible
Every moving ball leaves a colored trail. The trail follows the ball's trajectory as it travels
through the environment.

We created two simultaneous views of the same simulation.

In the first view, the trajectories remain visible. As collisions and generations accumulate, the
display develops an increasingly dense network of colored paths.

In the second view, trails from later generated balls gradually fade. The original reference
trajectories remain visible, while recent secondary movements are easier to distinguish.

The two views contain the same underlying events. A collision occurring in one view is the same
collision displayed in the other.

The difference is how much of the recorded trajectory history remains visible.

The persistent view allows us to examine the accumulated progression. The fading view allows
us to follow continuing motion without the entire earlier history remaining equally prominent.

Together, they make it possible to observe both the development of the system and its current
activity.
### 2.6 Introducing an observer
Once the simulation could generate objects and preserve their histories, we introduced another
type of moving object.

This object is identified as D and represents an observer.

D has its own position and movement within the environment. Unlike the ordinary balls, D is
programmed to seek and encounter the original generated c. It does not participate in the
collisions that generate new ordinary balls.

When D encounters c, the simulation records the encounter.

The record identifies the observer, the object encountered, the time and location of contact, and
the current state of c. It also retains a reference to the original A–B collision that produced c.

For example, D may encounter c several seconds after its creation. Although the original
collision has already occurred, its record allows the encounter to be associated with that earlier
event.

If c has changed size before the encounter, that state is also recorded.

The observer therefore encounters an object with an existing history.

The programmed encounters provide access to that history. Whether an observer subsequently
asks a question about the encountered object is a separate matter that we will examine later in the
paper.
### 2.7 Extending the environment into three dimensions
The initial experiment used a two-dimensional square. We subsequently extended the
environment into a three-dimensional cube.

The additional dimension allows objects to move in depth as well as horizontally and vertically.

Each ball's position is now represented by three coordinates:


$$
\mathbf{r}=(x,y,z)
$$

Its movement is represented by three velocity components:


$$
\mathbf{v}=(v_x,v_y,v_z)
$$

Collisions are calculated using the objects' positions in three-dimensional space. Balls reflect
from the six faces of the cube.

The computer displays the cube as a projection onto a two-dimensional screen, allowing viewers
to see the three-dimensional motion.

This extension changes the available trajectories and the opportunities for collision. Two
projected paths may appear to cross on the screen while the objects occupy different depths
within the cube.

The underlying rules for collision-generated objects and subsequent growth remain the same.
### 2.8 Introducing multiple observers
The next development added two observers, producing three distinct observer identities.

Each observer is assigned a different color:
- D1 is violet.
- D2 is orange.
- D3 is white.

All three are programmed to seek and encounter the same original c.

Each observer moves independently and maintains its own encounter history. An encounter by
D1 is recorded separately from an encounter by D2 or D3.

The original c retains its identity and recorded origin throughout these encounters.

This arrangement allows us to examine one generated object being encountered by multiple
observers at different times and locations.

The observers share the same environment and encounter the same object, while their individual
histories remain distinguishable.
### 2.9 Experimental controls and reproducibility
The simulation was written in Python using numerical calculations for movement, collision
detection, object generation, and event recording.

The environment has a side length of 380 simulation units. Motion is updated in discrete time
steps, and a fixed pseudorandom seed of 14 is used so that the same initial settings can reproduce
the same computational sequence.

A qualifying collision requires contact under the program's collision conditions. The software
separates overlapping balls, applies a brief contact cooldown, and attempts to position each
newly generated ball without overlapping existing objects.

The implementation limits the ordinary-ball population to 88. Once that limit is reached, existing
balls continue moving and colliding without further population growth.

These conditions establish the computational environment in which the recorded results were
produced.

The experiments were preserved as separate versions. The initial square experiment was
followed by the single-observer experiment, the three-dimensional cube, and the three-observer
arrangement.

A later version introduced controls for the duration and speed of the simulation. This allowed us
to produce a longer, slower presentation while retaining the same collision, generation, and
observer rules.

Each version preserves its source code and recorded event data. The accompanying materials
allow the reader to examine the methods, reconstruct the experiment, and compare the resulting
observations.

With the experimental procedure established, we can now examine what occurred as the system
developed, beginning with the first collision between A and B.
## 3. Experimental Results and Observations
### 3.1 The first interaction
The experiment begins with two balls moving toward one another inside the square. A is green,
and B is blue. Their paths bring them together, and the first collision occurs approximately 0.9
seconds after the simulation begins.

At that moment, the program generates a third, smaller ball, c.

The system now contains three independently moving objects. A and B continue along their
resulting trajectories, while c begins moving from a location associated with the collision.

This is the first observable change in the system's population. The original interaction has
produced a new participant, and the simulation has recorded when and where that occurred.

From this point forward, the movement of c creates additional opportunities for interaction.
### 3.2 The development of the system
As the simulation continues, collisions occur between existing balls. Each qualifying collision
can generate another small ball, adding a new participant to the environment.

Some of these smaller balls subsequently collide with other objects and grow to normal size.
Their appearance changes from red to yellow, making the transition visible.

The growing population produces an increasingly complex pattern of movement.

In the first experiment, which ran for 17 seconds, the system developed from two balls to 88. Of
these, 86 were generated by collisions during the simulation. The program recorded 1,301
qualifying collision events.

The population reached the program's limit of 88 balls. Collisions continued after that limit was
reached, although the program no longer added new balls.

The persistent-history view became increasingly dense as trajectories accumulated. Green and
blue paths from the original objects remained visible among the red and yellow paths produced
by later generations.

In the fading-history view, the recent movements remained easier to follow because older
secondary trails gradually disappeared.

The two views revealed different aspects of the same process.

One showed the accumulated history of interactions. The other emphasized the objects still
moving and interacting within the environment.

What appeared visually as an increasingly tangled collection of paths was generated through
repeated applications of the same collision and generation rules.
### 3.3 Following one generated object
The next experiment introduced observer D while preserving the original two-dimensional
movement and collision sequence.

D was programmed to seek the first generated ball, c.

The important feature of this arrangement is that c already has a history when D first encounters
it. Its origin can be traced to the collision between A and B.

During the 17-second experiment, D encountered c nine times.

The first encounter occurred approximately 2.73 seconds into the simulation, when c was still
small and red.

Later, at approximately 6.13 seconds, c participated in a collision with another ordinary ball.
Under the programmed growth rule, this interaction increased its size to that of a normal ball,
changing its appearance to yellow.

At approximately 7.40 seconds, D encountered the same object again, now in its enlarged state.

These observations establish a useful relationship.

The object encountered at 2.73 seconds and the object encountered at 7.40 seconds are the same
generated participant. Its state has changed, and its history includes that transformation.

The encounter records identify the object's condition at each observation and retain its
connection to the original A–B collision.

This makes it possible to examine an object at different moments without losing the history that
identifies its origin.
### 3.4 What changed when depth was introduced
The third experiment extended the environment from a square into a three-dimensional cube.

The balls could now move along X, Y, and Z coordinates. Their paths were no longer confined to
a single plane.

The projected visualization made the additional spatial dimension visible. Objects could pass in
front of or behind one another, and paths that appeared to intersect on the screen did not always
correspond to physical collisions within the simulated cube.

Under these conditions, the 17-second run produced seven ordinary balls, including five
generated balls, and recorded five qualifying collisions.

D encountered the original c six times.

The original c remained small and red throughout this run because it did not experience a
qualifying collision that triggered growth.

The difference between the two-dimensional and three-dimensional results was substantial.

The square experiment reached 88 balls, while the cube experiment contained seven after the
same recorded duration.

This comparison shows how changing the available space for movement changes the resulting
interaction history. The objects followed the same general collision and generation rules, but the
three-dimensional trajectories produced a different sequence of encounters.
### 3.5 Three observers encountering the same object
The fourth experiment retained the cube and introduced two additional observers.

The system now contained three observers, each with a distinct color and identity.

All three were programmed to seek the same original c. Each moved independently and recorded
its encounters separately.

Over the 17-second experiment, the observers registered sixteen encounters with c:
- D1, violet: six encounters.
- D2, orange: five encounters.
- D3, white: five encounters.

The underlying ordinary-ball population remained at seven, with five births and five qualifying
collisions.

The significant observation concerns the relationship between the object and its observers.

Each observer encountered the same c, whose history originated in the same A–B collision.

Yet each observer had a different sequence of encounters. Their records differed in time,
location, and observer identity.

The introduction of additional observers did not change the recorded ordinary-ball interaction
sequence. It added independently identifiable encounters with a shared object.

The experiment therefore made two histories visible at the same time: the history of c itself and
the separate histories of the observers encountering it.
### 3.6 Observing the progression over a longer period
The fifth experiment extended the presentation to 60 seconds and reduced movement speed to
half the configured normal rate.

The longer duration allowed more of the progression to be seen without requiring the viewer to
follow the faster movements of the earlier experiments.

The recorded run used a 12-frame-per-second simulation rate and retained the three observer
identities.

By the end of the run, the system contained ten ordinary balls, including eight generated balls,
and had recorded eight qualifying collisions.

The three observers registered 47 encounters with c:
- D1: sixteen encounters.
- D2: sixteen encounters.
- D3: fifteen encounters.

The original c remained small and red throughout this run.

Because the simulation's duration, movement speed, and frame rate differed from the preceding
experiment, this run represents a separate sequence of simulated events rather than a slowed
recording of the earlier sequence.

The persistent-history view accumulated trajectories over the longer period. The fading-history
view continued to distinguish recent secondary movements from the original reference paths.

The additional running time made the continuing relationship between the original collision, the
generated object, and the observers easier to follow.
### 3.7 Comparing the results
The five experiments produced the following recorded results.

                                                      Ordinary                        Observer
       Experiment         Environment Duration                     Collisions
                                                        balls                        encounters
## 1. Initial generation   2D square        17 s       88             1,301        0
## 2. Single observer      2D square        17 s       88             1,301        9
## 3. Three-dimensional
                        3D cube          17 s       7              5            6
motion
## 4. Three observers      3D cube          17 s       7              5            16
## 5. Extended observation 3D cube          60 s       10             8            47
The table reports the results of the recorded executions, rather than averages across repeated
experimental trials. The fifth experiment also used a 0.50 movement-speed multiplier and a
different frame rate.

The comparison identifies several observable relationships.

First, the number of objects in the environment changes as collisions generate additional
participants.

Second, an object's state can change through subsequent interaction while its identity and
recorded origin remain traceable.

Third, changing the dimensionality of the environment produces a different history of movement
and collisions under the programmed rules.

Fourth, multiple observers can encounter the same object independently, producing distinct
encounter records linked to a shared origin.

Finally, the events can be examined at different scales of time. An individual collision may
occupy only a fraction of a second, while its resulting object and associated history continue to
develop throughout the experiment.
### 3.8 What the observations reveal
Across the five experiments, the same fundamental progression can be followed.

Two objects interact. Their interaction produces a result. That result becomes part of the
environment and can participate in further interactions. Its state and circumstances may change,
while its origin remains identifiable through the recorded history.

Observers can later encounter the result at different times and in different conditions.

Each encounter provides information about the object's current state and a connection to the
events that preceded it.

The resulting visual system becomes increasingly complex as interactions accumulate. Yet the
individual events remain connected through identifiable relationships.

The experiment thus makes it possible to examine how an originating event produces a
continuing history, and how different observers can encounter that history from different
positions in time and space.

These observations provide the foundation for the next part of the investigation: how an observer
uses information about an event, why different observers may ask different questions, and what
those questions contribute to their understanding of the same occurrence.
## 4. Space, Time, and Observation
### 4.1 Where and when an event occurs
Every interaction in the experiment occurs at a particular location and moment. The balls move
through space, their paths intersect, and collisions produce new objects. As the simulation
continues, each interaction becomes part of a developing history.

To describe this progression, we need to account for both space and time.

The three spatial dimensions identify where an object is located:
- X describes its horizontal position.
- Y describes its vertical position.
- Z describes its depth.

A fourth dimension, T, identifies when the object occupies that position.

Together, these provide four coordinates:


$$
(x,y,z,t)
$$

For example, if A and B collide at position (100, 150, 200) when the simulation clock reaches
five seconds, the interaction can be recorded as:


$$
e=(100,150,200,5)
$$

The first three values establish the location, while the fourth establishes the time.

This gives every recorded collision a position in space and time. Two collisions may occur at the
same location but at different moments. Likewise, two events may occur at the same moment but
in different locations.

Both their spatial and temporal coordinates are necessary to distinguish where and when they
occurred.

The experiment uses three spatial dimensions and one temporal dimension. Time is already
present in the simulation as successive computational updates. Expressing it as a fourth
coordinate makes its relationship to the recorded events explicit.
### 4.2 The originating event and its history
Return to the first collision between A and B.

Their interaction produces c, the smaller object that begins moving independently within the
environment.


$$
A+B\rightarrow c
$$

The collision occurs at a particular location and moment. That establishes the origin of c's
history.

As c moves through the environment, its position changes with time. We can describe its
position at any recorded moment as:


$$
\mathbf{r}_c(t)=(x_c(t),y_c(t),z_c(t))
$$

This tells us where c is at time t.

The complete movement of c forms a trajectory through space over time. If c collides with
another object, that interaction becomes another event in its history. If its size changes, the
transition is recorded at the time it occurs.

Every subsequent event adds to the progression that began with the original collision.

We can therefore distinguish the complete originating event, which includes A, B, their
interaction, and the resulting c, from the individual object that continues moving afterward.

The complete originating event is identified as ABc. The lowercase c identifies its generated
product.

As time progresses, c may participate in another interaction, occupying the role of A or B and
contributing to the generation of another c.

The later event has its own location, time, participants, and resulting history.

The relationship between these events creates a traceable sequence. Each event can be examined
individually while remaining connected to the events that preceded it.
### 4.3 Observing an event at different moments
Consider what happens when an observer encounters c.

The observer occupies a position in the same environment and encounters c at a particular
moment. The encounter can be recorded with its own spatial and temporal coordinates.

Suppose three observers encounter the original c at different times.

D1 encounters c at twelve seconds. D2 encounters it at twenty-five seconds. D3 encounters it at
forty seconds.

All three encounters concern the same generated object, but each occurs at a different moment in
its history.

At twelve seconds, c has already traveled away from its originating collision. By twenty-five
seconds, it may have experienced additional interactions. By forty seconds, its position and
condition may have changed again.

The observers encounter c under the conditions present at their respective moments.

The simulation's retained history allows each encounter to be connected to the original event.

The difference between an object's current condition and its recorded history is important. An
observer encounters the object at a particular time, while the history describes how it reached
that condition.

A second observer may encounter the same object later and have access to information that was
unavailable during the earlier encounter.

Both observations concern the same originating event, while the circumstances of observation
differ.
### 4.4 A traffic accident as an example
The relationship becomes easier to recognize in an ordinary event.

Imagine two vehicles approaching an intersection. They collide at a particular location and time.

The collision produces consequences: damaged vehicles, changes in their positions, physical
traces on the roadway, and effects on the people involved.

These consequences develop from the originating interaction.

Now consider three people who encounter the accident.

A bystander witnesses the collision as it happens. The bystander sees the vehicles approaching,
hears the impact, and observes what happens immediately afterward.

A traffic officer arrives several minutes later. The officer sees the vehicles in their resulting
positions, observes physical evidence, and may obtain accounts from the people present.

An insurance adjuster examines the accident days later. The adjuster may encounter photographs,
vehicle damage, repair estimates, witness statements, and the officer's report.

Each person is examining information connected to the same originating event.

Their positions in space and time differ.

The bystander has access to the unfolding collision. The officer encounters its immediate
aftermath. The adjuster encounters evidence and records produced during and after the event.

The original collision has one history, while the information available to each observer depends
on when, where, and how the observer encounters its consequences.

This relationship is similar to what occurs in the computational experiment.

The original c carries an identifiable history. The observers encounter it at different points in that
history. Each encounter provides information associated with a particular moment, while the
retained records connect that moment to the object's origin.
### 4.5 From observation to information
The addition of time allows us to distinguish the originating event from the later encounters
through which information about that event becomes available.

But encountering information introduces another relationship.

The bystander, traffic officer, and insurance adjuster may each become interested in different
aspects of the accident.

The bystander may want to know whether anyone was injured. The officer may want to establish
how the collision occurred. The adjuster may want to determine the resulting damage and its
financial consequences.

These questions direct attention toward different parts of the same history.

A question about injuries draws upon information about the people involved. A question about
the cause of the collision draws upon vehicle movements, roadway conditions, and the sequence
of events. A question about financial consequences draws upon damage assessments, repair
costs, and insurance arrangements.

Each observer may organize information differently according to the question being asked.

The accident remains the common originating event. The questions establish different
relationships between that event and the observers examining it.

An observer may also encounter the accident without asking a question. The encounter provides
an opportunity for inquiry, while the decision to ask a question is a further step.

This distinction allows us to follow a progression from an event occurring to information
becoming available and, potentially, becoming the subject of inquiry.
### 4.6 What the fourth dimension contributes
Time provides the continuity connecting the original interaction to the later observations.

Without identifying when events occur, we could describe the positions of objects but would lose
the order in which their interactions developed.

With time included, we can follow how an object emerges, moves, changes state, and becomes
available to different observers.

The four-coordinate description also allows the same event history to be examined from different
observational positions.

The underlying history remains traceable, while the information accessible at each encounter
reflects the observer's position in space and time.

In the experiment, this relationship is represented through trajectories, collision records, object
identities, and observer encounter histories.

In the traffic accident example, it appears through the different evidence available to a witness,
an investigating officer, and an insurance adjuster.

Both examples show how an originating event can support multiple observations distributed
across space and time.

The next question concerns what an observer does with the information made available through
an encounter.

If several observers can encounter the same event and ask different questions about it, how
does each question contribute to the formation of that observer's understanding?

That relationship leads us from the observation of events to the investigation of questions and
information formation.
## 5. Questions and the Formation of Information
### 5.1 From encountering an event to asking a question
In the preceding sections, we followed an event from its origin through subsequent interactions
and observations. We established that an event occurs at a particular position in space and time,
produces consequences, and develops a history that can be encountered by different observers.

We now turn to what happens when an observer asks a question about that event.

Consider the traffic accident introduced earlier. A bystander sees two vehicles collide. The
collision has occurred, and the bystander has witnessed it. At this moment, the bystander has
information about the event, including the vehicles' movements, the impact, and its immediate
consequences.

The bystander may continue watching without asking a question. Alternatively, something about
the event may attract their attention.

Perhaps one driver has not exited the vehicle.

The bystander asks, "Is the driver injured?"

This question establishes a particular relationship between the observer and the event. The
collision contains many observable details, but the observer is now interested in information
concerning the driver's condition.

The question directs attention toward a specific part of the event and its consequences.

The observer may look for movement inside the vehicle, listen for a response, or approach to
determine whether assistance is needed.

The event has become the subject of a particular inquiry.

This distinction matters because observing an event and asking a question about it are separate
occurrences. The accident happened independently of the bystander's question. The question
arises in relation to information the observer has encountered.
### 5.2 One event, different questions
Now consider the traffic officer arriving at the accident scene.

The officer encounters the same originating event through its consequences. The damaged
vehicles, their positions, roadway conditions, and witness accounts provide information about
what happened.

The officer may ask, "How did the vehicles collide?"

This question directs attention toward the sequence of movements leading to the impact.

The officer may examine vehicle positions, roadway markings, traffic signals, and statements
from the people involved. These observations contribute to an account of how the collision
occurred.

The insurance adjuster may later encounter photographs, repair estimates, and other records
associated with the same accident.

The adjuster asks, "What damage resulted from the collision?"

That question directs attention toward another set of relationships, including the vehicles'
condition before and after the accident, the damage attributable to the impact, and the financial
consequences.

We now have three questions concerning one originating event:
- The bystander asks whether someone was injured.
- The traffic officer asks how the collision occurred.
- The insurance adjuster asks what damage resulted.

Each question identifies a different aspect of the event for examination.

The answers may draw upon overlapping evidence. The officer and adjuster may use the same
photographs. The bystander and officer may both have observed the vehicles immediately after
the collision.

Yet their questions organize the available information toward different purposes.

The original collision remains the common event connecting their inquiries.

Each observer develops an understanding of a particular relationship within that event's history.
### 5.3 The structure of a question
The questions in these examples have something in common. Each seeks information about an
identifiable aspect of an event.

We can examine this through six familiar interrogatives:

WHO, WHAT, WHERE, WHEN, HOW, and WHY.

These provide different ways of directing inquiry toward an event.

For the traffic accident, the questions might be:
- WHO: Who participated in or witnessed the collision?
- WHAT: What happened during the collision?
- WHERE: Where did the vehicles collide?
- WHEN: When did the collision occur?
- HOW: How did the vehicles come into contact?
- WHY: Why did the collision occur?

Each question directs attention toward a relationship that may be examined through available
information.

The questions can also lead to one another.

An observer asking what happened may discover that two vehicles collided at an intersection.
That information may lead to a question about how the vehicles approached one another.

An investigation into their movements may reveal that one vehicle entered the intersection
against a traffic signal. This may lead to further questions concerning the driver's actions,
visibility, or roadway conditions.

As inquiry proceeds, information obtained through one question can become relevant to another.

The process develops through a sequence of questions and the information associated with their
investigation.

The six interrogatives provide a structure for examining the event from different informational
directions. The observer's particular question determines which direction becomes the immediate
subject of inquiry.
### 5.4 Returning to the computational experiment
The same relationship can be examined in the simulation.

Recall that two original objects, A and B, collide and generate a smaller object, c.


$$
A+B\rightarrow c
$$

The program records the circumstances of that interaction. The record identifies the original
participants, the time and location of the collision, and the resulting object.

As c moves through the environment, its history develops through subsequent movement and
possible collisions.

An observer, D1, later encounters c.

The encounter record identifies where and when D1 encountered the object and the condition of
c at that moment. It also connects c to the original collision that produced it.

Suppose D1 asks, "Where did this object originate?"

The recorded history provides information relevant to that question. The observer can trace c to
the original A–B interaction.

A second observer, D2, encounters c at another moment and asks, "What interactions has this
object experienced?"

That question directs attention toward c's subsequent history.

A third observer, D3, asks, "How did this object reach its present position?"

This question concerns the object's movement through space and time.

Each question concerns the same c, but selects a different relationship for examination.

The simulation provides the underlying movement, collision, and encounter records. The
questions in these examples illustrate how different observers could use that recorded
information.

The important relationship is between the history of the generated object and the different
questions observers may direct toward it.
### 5.5 The potential for a question
We can now examine a feature of the experiment that was present before any observer was
introduced.

When A and B collide, the interaction produces c.

At that moment, there is no observer asking where c came from, what it is, or how it will move.

Nevertheless, the interaction has occurred. The new object exists within the simulation, and its
history begins with the collision that produced it.

That history provides possible subjects for inquiry.

An observer might later ask about c's origin, its present condition, its movement, or its
subsequent interactions.

The questions have not yet been asked, but the originating event and the resulting object provide
something about which questions may arise.

This is the relationship we identify as the potential of a question.

Within the investigation, c represents a resulting state that may become the subject of inquiry.

The potential is associated with the interaction that produced c. The observer's question arises
later, through the observer's relationship with that resulting state and its history.

The distinction can be expressed through the progression:


$$
A+B\rightarrow c
$$

The interaction produces c.

An observer D may subsequently encounter c and originate a question concerning it.

The question depends on the observer's inquiry into c, while c's origin remains the earlier
interaction between A and B.

This relationship also allows the process to continue.

A generated c can participate as an object in another interaction, occupying the role of A or B.
That interaction can produce a further c, with its own origin and history.

As interactions accumulate, additional states become available as possible subjects of inquiry.

The simulation makes the generation of these states visible. The theoretical investigation asks
what their availability means for the origination of questions.
### 5.6 How information is formed in relation to the observer
Return once more to the three observers of the traffic accident.

All three are concerned with the same originating event.

The bystander, traffic officer, and insurance adjuster each encounter information connected to
that event, but their questions direct attention toward different relationships.

The bystander may develop an understanding of the accident through its immediate human
consequences.

The traffic officer may develop an understanding through the sequence of events and the
evidence concerning how the collision occurred.

The adjuster may develop an understanding through the resulting damage, its documented
causes, and its financial consequences.

Each understanding is formed through a relationship between the observer, the available
information, and the question being investigated.

The event's history connects these different accounts. The observer's question determines which
aspects of that history become the focus of inquiry.

Information formed through one question may become relevant to another observer's
investigation. An officer's reconstruction may inform an insurance assessment. A bystander's
observations may contribute to the officer's understanding of the accident.

In this way, different inquiries can remain distinct while drawing upon the same originating
event.

The resulting information is associated with the observer's particular relationship to that event.

For one observer, the accident may be understood primarily through the condition of the people
involved. For another, it may be understood through the sequence of actions that produced the
collision. For a third, it may be understood through the resulting damage and financial
consequences.

Each observer has formed an account of the same occurrence through a different question.
### 5.7 From information to understanding
The experiment begins with an interaction and follows its consequences over time.

The introduction of observers adds another relationship: the same originating event can become
the subject of different inquiries.

The computational records provide information about what occurred. An observer's question
directs attention toward particular relationships within that information.

Through investigation, the observer may develop an understanding of the event.

That understanding becomes part of what the observer knows about the occurrence and may
influence how subsequent information is interpreted.

The progression can therefore be followed from the originating interaction, through the resulting
history, to the observer's question and the information formed through inquiry.

This brings us to the broader proposition motivating the investigation.

If different observers can form different informational understandings through their
questions about the same event, what relationship exists between those understandings and
what each observer recognizes as reality?

The next section examines that question using the computational observations, the traffic
accident example, and the distinction between an event's history and the information formed by
those who inquire into it.
## 6. Information and the Reality Recognized by an Observer
### 6.1 One event, different understandings
In the previous section, we examined how different observers can ask different questions about
the same event. We now consider what happens to the information formed through those
questions.

Return to the traffic accident.

Two vehicles collide at an intersection. The collision occurs at a particular location and moment,
producing consequences that continue beyond the initial impact.

The bystander, traffic officer, and insurance adjuster all encounter information concerning that
occurrence.

Each observer approaches the event from a different position in space and time. Each may ask
questions that direct attention toward particular aspects of what happened.

Consider the bystander who witnesses the collision and asks whether a driver has been injured.

The bystander observes the driver leaving the vehicle, speaking to another person, and walking
toward the sidewalk. These observations provide information relevant to the question.

The bystander may conclude that the driver is conscious and able to walk.

The traffic officer arrives later and investigates how the vehicles collided. The officer examines
the roadway, vehicle positions, traffic signals, and available witness accounts.

From this information, the officer may establish a sequence describing how the vehicles
approached the intersection and came into contact.

The insurance adjuster examines the damage and associated records. The adjuster may establish
which parts of each vehicle were damaged, what repairs are required, and the resulting financial
consequences.

All three observers have developed an understanding of the accident.

The bystander's understanding concerns the immediate condition of a person involved. The
officer's understanding concerns the sequence of events. The adjuster's understanding concerns
the physical and financial consequences.

Each account originates from information associated with the same collision.

Yet the resulting understandings are different because the observers asked different questions.
### 6.2 How a question contributes to an understanding
A question directs inquiry toward a particular relationship within the information available about
an event.

When the bystander asks whether the driver is injured, the question identifies the driver's
condition as the subject of inquiry.

The observer looks for information relevant to that condition.

When the officer asks how the collision occurred, the question identifies the sequence of vehicle
movements as the subject of inquiry.

The officer examines evidence relevant to reconstructing that sequence.

When the adjuster asks what damage resulted, the question identifies changes in the vehicles'
physical condition and their financial consequences.

In each case, a question establishes a direction for investigation.

The observer gathers information, examines relationships, and may arrive at an understanding.

This process can be described through three connected elements:
- The event: What occurred and the history associated with it.
- The question: The relationship the observer seeks to understand.
- The resulting information: What the observer establishes through inquiry.

The resulting information becomes part of the observer's understanding of the event.

An observer may also encounter information that changes an earlier understanding. A witness
may recall an additional detail. A photograph may establish a vehicle's position more precisely.
A later inspection may reveal damage that was initially overlooked.

The understanding can therefore develop as further information becomes available.

The question provides a relationship through which information is sought, examined, and
incorporated into what the observer understands.
### 6.3 What the observer recognizes as reality
Consider the bystander after witnessing the accident.

The bystander leaves the scene with an understanding of what happened. That understanding
includes the collision, the driver's apparent condition, and the events immediately following the
impact.

If asked to describe the accident, the bystander can provide an account based on those
observations.

For the traffic officer, the accident has another informational structure. It includes the
reconstructed sequence, the evidence examined, and the relationships established during the
investigation.

For the insurance adjuster, the accident is represented through damage, documentation,
assessments, and associated financial consequences.

Each observer recognizes the accident through the information formed during their encounter
and inquiry.

This leads to the proposition we are investigating:

[conjecture] The formation of information through an observer's question may constitute
what that observer recognizes as a form of reality.

In this proposition, a form of reality refers to the event as it becomes understood through the
information available to a particular observer.

The bystander recognizes an accident involving people whose safety may be at risk.

The officer recognizes an occurrence with a sequence of actions and evidence that can be
investigated.

The adjuster recognizes an event that produced damage and financial consequences.

These understandings arise from the same originating occurrence.

They can coexist because they concern different relationships within its history.

An account of the driver's condition does not replace an account of the vehicles' movements. An
assessment of the resulting damage does not remove the human consequences witnessed at the
scene.

The different accounts can each contribute accurate information concerning the same event.

The possibility being examined is that the observer's question participates in forming the
informational account through which the event becomes recognizable to that observer.
### 6.4 The role of the originating event
The relationship between these different understandings becomes clearer when we return to the
origin of the accident.

Before the bystander, officer, or adjuster begins an inquiry, the vehicles have already collided.

The occurrence has a location, a time, participating objects, and physical consequences.

In the notation introduced earlier:


$$
A+B\rightarrow c
$$

A and B represent the participating objects, and c represents the resulting product of their
interaction.

The complete occurrence, identified as ABc, includes the participants, their interaction, and the
resulting product.

The event's history provides a common reference for subsequent observations.

An observer may encounter one consequence of the accident without directly witnessing the
collision. The officer may examine physical traces left behind. The adjuster may examine
photographs and recorded assessments.

These observations can be associated with the same originating event through their histories.

This allows information formed at different moments to remain connected.

The observer's understanding develops in relation to the event, while the event's history provides
the basis for examining that understanding.

This distinction also explains why different observers can investigate different questions without
requiring different originating accidents.

There is one shared occurrence and a continuing history from which multiple informational
accounts can develop.
### 6.5 The importance of space and time
The fourth dimension introduced in Section 4 becomes particularly important when considering
these observer-specific understandings.

The bystander witnesses the accident during its occurrence. The officer may investigate minutes
afterward. The adjuster may examine its consequences days later.

Each observer encounters information associated with a different point in the event's history.

The information available at one moment may differ from what becomes available later.

A vehicle's position immediately after impact may be visible to the bystander. The officer may
document that position before the vehicle is moved. The adjuster may subsequently encounter
the position only through photographs and reports.

The information has passed through a sequence of observations and records.

Its relationship to the original event remains important because that history identifies where the
information originated.

The spatial and temporal coordinates of an encounter therefore help establish the circumstances
under which information became available.

In the computational experiment, each observer encounter is recorded with its position and time.

The original generated object, c, also has a recorded origin.

This allows us to distinguish the interaction that produced c from the later encounters through
which information about c becomes available.

The resulting records show how one object can have a continuing history while different
observers encounter it at different stages of that history.
### 6.6 Returning to the three-observer experiment
The three-dimensional experiment provides a visual arrangement in which these relationships
can be followed.

A and B collide, producing c.

The generated object begins moving through the cube. Its origin is recorded, and its subsequent
movement becomes part of its history.

Three observers, D1, D2, and D3, move within the same environment.

Each is programmed to encounter the original c.

The observers have different identities and trajectories. Their encounters occur at different
positions and times.

The program records these encounters independently.

[established] The experiment demonstrates that multiple observers can encounter the same
generated object while maintaining distinct encounter histories linked to its common origin.

The colored trajectories make this relationship visible.

The persistent-history view shows the accumulated movements and interactions. The fading-
history view emphasizes more recent secondary movement while retaining the original reference
trajectories.

The viewer can identify the object being encountered, follow its history, and distinguish the
observers through their individual colors and movements.

The computational records establish the encounters. The questions an observer might ask are
considered separately.

Suppose D1 is interested in c's origin, D2 in its movement, and D3 in its current condition.

Each question concerns information available through the same object and its recorded history.

The resulting informational accounts would differ according to the relationships investigated.

This is the observer-specific information formation proposed by the investigation.
### 6.7 Information becoming part of subsequent interactions
The progression can continue beyond an observer's initial understanding.

In the traffic accident example, the officer's investigation produces a report.

That report becomes an informational object that another person can encounter.

The insurance adjuster may use it alongside photographs, damage estimates, and other records.

The information formed through the officer's investigation now participates in a further
interaction.

We can describe that relationship using the same notation introduced at the beginning of the
paper.

Two existing informational objects or states participate in an interaction, producing a resulting
state.


$$
A+B\rightarrow c
$$

The roles of A and B are occupied by the participating information at that stage of the process.

The resulting c may subsequently participate in another interaction, again occupying an A or B
role.

In this way, information formed through one investigation can become part of the conditions for
another.

The officer's report may contribute to the adjuster's understanding. The adjuster's assessment
may subsequently contribute to another inquiry.

Each interaction produces a result associated with its generating conditions.

The process develops through successive informational relationships, just as the computational
experiment develops through successive interactions among moving objects.

[conjecture] This recurring structure offers a way to examine how information formed through
one inquiry can become part of the conditions from which further inquiry develops.

The relationship is significant because the progression does not end with one observer or one
question.

The information formed through an inquiry can itself become something that another observer
encounters, examines, and questions.
### 6.8 What the experiment allows us to consider
We began with a simple collision between two moving objects.

The interaction produced a third object, which continued moving and participating in subsequent
events.

We then introduced observers who could encounter that object at different positions and
moments in its history.

The simulation made these relationships visible through object movement, generation, state
changes, trajectories, and recorded encounters.

The traffic accident example allowed us to examine another part of the progression: different
observers may ask different questions concerning the same occurrence and form different
informational understandings from their inquiries.

Together, these relationships provide the basis for the proposed connection between information
formation and the reality recognized by an observer.

An event occurs and develops a history. An observer encounters information associated with that
history. A question may direct the observer toward a particular relationship. The resulting
inquiry may establish information that becomes part of the observer's understanding.

Different observers can follow different questions through the history of the same event.

[conjecture] The form of reality recognized by an observer may therefore be understood
through the information constituted in that observer's relationship with an event.

This is the possibility the investigation places before the reader.

The computational experiments establish the movement, generation, transformations, and
recorded encounters. The theoretical proposition concerns what the formation of information
through an observer's question may mean for the observer's understanding of reality.

The next section brings these observations and relationships together, examining what has been
established, what remains proposed, and what questions follow from the investigation.
## 7. Discussion: What the Experiments Reveal
### 7.1 From a simple interaction to a developing system
The investigation began with two moving objects and a bounded environment. The objects
followed straightforward rules governing movement, reflection, collision, and the generation of
additional objects.

When A and B first collided, the interaction produced a smaller object, c.

This introduced a new participant into the system. The resulting object moved independently,
could encounter other objects, and could contribute to further interactions.

As the experiment continued, the number of objects increased. Their movements produced
additional collisions, and those collisions generated further objects.

The original two-dimensional simulation developed from two objects to 88 within seventeen
seconds.

[established] This result demonstrates how repeated application of a small set of computational
rules can produce an expanding population of interacting objects with increasingly complex
trajectories.

The result is important because the complexity can be traced to identifiable events.

Each generated object has an origin. Each qualifying collision occurs at a recorded position and
time. Each subsequent interaction becomes part of the developing history.

The full visual pattern may be difficult to follow at once, while the individual events remain
describable through the rules that produced them.

The experiment therefore allows us to examine the developing system at two scales: the
individual interaction and the accumulated history of many interactions.

Both describe the same process.
### 7.2 A resulting object becomes a participant
One relationship deserves particular attention.

When A and B collide, the resulting c is produced by their interaction.

Before that collision, c was absent from the simulation. Afterward, c is an object with its own
position, motion, and recorded origin.

The resulting object can then participate in another interaction.

Consider a simple sequence:


$$
A_1+B_1\rightarrow c_1
$$

The first interaction produces c₁.

Now suppose c₁ encounters another object, B₂. In this interaction, c₁ occupies the participating
role of A:


$$
c_1+B_2\rightarrow c_2
$$

The second interaction produces c₂.

The first resulting object has become a participant in the second event.

The process can continue, with c₂ participating in a later interaction.

The labels A and B therefore identify participating roles, while each resulting c retains its own
identity and originating history.

This distinction allows us to follow the progression across multiple events.

[established] The computational experiments implement this recurring participation. Generated
objects remain active and can contribute to subsequent collision-generated events.

[conjecture] The same abstract relationship may provide a useful way to examine information
formation: a result produced through one interaction can become part of the conditions for
another interaction.

For example, a traffic officer's report is produced through an investigation of an accident. That
report can subsequently become information used by an insurance adjuster.

The report is a result of one informational process and a participant in another.

The relationship allows us to examine how information develops through successive interactions
while retaining a connection to its origin.
### 7.3 Why an event's history matters
Consider two generated objects that appear identical at a particular moment.

They may have the same size, color, position, or direction of movement.

Yet they may have originated from different collisions.

One may have been produced by the original interaction between A and B. Another may have
been generated later by two objects whose own histories extend through several earlier
interactions.

Their present appearances alone may not distinguish those histories.

The simulation addresses this by retaining identifying information about each generated object
and the event that produced it.

For the original c, the record includes its connection to the A–B collision. Later encounters can
therefore be associated with that particular originating event.

[established] The preserved records allow the experiment to distinguish the current state of an
object from the recorded interaction that produced it.

This becomes significant when an observer encounters the object.

An observer can encounter c in its current condition and, through the retained records, examine
how it arrived at that condition.

The current state provides one part of the information. The history provides another.

The traffic accident offers a familiar example.

Two damaged vehicles may have similar visible conditions while having experienced different
sequences of events. Establishing what happened requires information about their respective
histories.

Likewise, two observers examining the same accident may possess different portions of its
recorded history.

The relationship between a current observation and the earlier events that produced it is therefore
central to understanding what the observation represents.
### 7.4 What multiple observers add
The introduction of three observers allows us to examine a relationship that was absent from the
initial experiment.

The original generated c remains identifiable, while D1, D2, and D3 encounter it through
separate movements and at different moments.

Each observer maintains a distinct encounter history.

The recorded three-observer experiment produced sixteen encounters with the original c. Those
encounters were distributed across the three observer identities, while their records remained
connected to the same originating A–B interaction.

[established] The experiment demonstrates that multiple observers can encounter a shared object
and produce separately identifiable encounter records without changing that object's recorded
origin.

The significance of this arrangement becomes clearer when we return to the traffic accident.

The bystander, traffic officer, and insurance adjuster are concerned with one event, although
their encounters and inquiries differ.

The bystander may observe the accident as it occurs. The officer may reconstruct the sequence
from physical evidence and witness accounts. The adjuster may examine its documented
consequences later.

Each observer encounters information related to the same event.

The available information may differ because the encounters occur at different positions and
times. The questions asked may also differ because each observer seeks to understand a different
relationship.

[conjecture] These distinctions provide a basis for examining how multiple observers can
develop different informational understandings of one shared occurrence.

The observers' accounts may overlap, contribute to one another, or address different aspects of
the event.

Their common reference is the history of the originating occurrence.
### 7.5 The relationship between an event and a question
We can now return to the central research question.

The collision between A and B produces c.

The resulting object exists within the simulation and has an identifiable history. That history can
become the subject of inquiry.

An observer may ask where c originated, how it moved, what interactions it experienced, or why
a particular event occurred.

These questions concern relationships associated with c and its history.

The originating interaction establishes the event from which those relationships develop.

The observer's question directs inquiry toward one of them.

This is where the concept introduced in Section 5 becomes relevant.

[conjecture] We propose that an interaction-generated result such as c can represent the
potential of a question because its existence and history provide relationships that an
observer may subsequently inquire into.

The potential arises through the originating interaction.

A question may arise later, when an observer directs inquiry toward that potential.

The observer may also encounter c without asking a question.

The possibility of inquiry and the occurrence of inquiry are therefore distinguishable.

This relationship can be followed in the traffic accident example.

The accident occurs before the officer investigates it. Its history contains relationships
concerning the participating vehicles, their movements, the location of impact, and the resulting
consequences.

The officer may subsequently originate a question about one of those relationships.

The question establishes what the officer seeks to understand.

The resulting investigation may produce information that becomes part of the officer's account of
the accident.

The sequence moves from an originating event to the possibility of inquiry, and from inquiry to
the formation of information.
### 7.6 From information to a form of reality
The different accounts formed by the bystander, officer, and adjuster bring us to the broadest
proposition of the investigation.

The three observers encounter the same accident.

Each may ask different questions, examine different evidence, and establish different
information about what occurred.

Their resulting understandings may be accurate within the relationships they have investigated.

For the bystander, the accident may be understood through its immediate human consequences.

For the officer, it may be understood through the sequence of events and the evidence associated
with the collision.

For the adjuster, it may be understood through damage, responsibility, and financial
consequences.

Each observer forms an informational account of the originating event.

These accounts become part of what each observer understands about the accident.

The observation motivating this paper is that different understandings can develop from the
same event without requiring different originating events.

The questions asked by each observer contribute to the formation of those understandings.

This leads to the proposition:

[conjecture] Information formed through an observer's question may contribute to what
that observer recognizes as a form of reality.

The phrase a form of reality refers here to the event as understood through the information
established by an observer.

The investigation does not begin by assigning a universal definition to reality. It examines how
an observer forms information about an occurrence and how that information contributes to what
the observer recognizes and understands.

The computational experiments provide a visible model of the underlying progression from
interaction to observation.

The traffic accident example extends the discussion to the questions through which people form
different informational accounts of a shared event.

Together, these provide a way to examine the proposed relationship between questions,
information, and observer-specific understanding.
### 7.7 What remains to be investigated
The experiments establish the behavior of the programmed system: objects move, collide,
generate further objects, change state, and develop histories that can be encountered by one or
more observers.

The theoretical investigation extends from those observations to the possible relationship
between interaction-generated states and the origination of questions.

Several questions now follow from the relationships examined in this paper.

What distinguishes an event that becomes the subject of a question from the many events an
observer encounters without inquiry?

How does an observer's question determine which information about an event is examined?

When different observers investigate the same originating event, what makes their informational
accounts distinct, and what allows those accounts to remain connected to a shared history?

How does information established through one inquiry become part of the conditions for
subsequent inquiry?

And what does this progression reveal about the relationship between information formation and
the reality recognized by an observer?

These questions identify the next relationships to be examined.

The computational experiments provide reproducible event histories and observer-encounter
records. The conceptual examples provide a way to examine how questions participate in the
formation of information.

The investigation can therefore proceed from an observable sequence of interactions toward a
more precise examination of inquiry itself.
### 7.8 Discussion summary
The investigation has followed one relationship through several stages.

Two objects interact, producing a result. That result becomes part of the system and can
participate in further interactions. Its history develops as those interactions continue.

Observers encounter the resulting object at particular positions and times. Each encounter
provides access to information associated with its current condition and recorded origin.

An observer may then direct a question toward that information.

The question identifies a relationship for inquiry, and the resulting investigation may contribute
to the observer's understanding of the event.

Different observers may form distinct understandings while remaining connected to the same
originating history.

The central observation is that an event, its history, an observer's encounter, and the
information formed through a question are connected stages of a developing relationship.

The computational experiments make the earlier stages visible and reproducible. The theoretical
proposition examines what the later stages may reveal about question origination and observer-
specific informational reality.

The final section brings these findings together and states the conclusion of the investigation.
## 8. Conclusion: From Interaction to Information
### 8.1 What the investigation established
This investigation began with a simple event: two objects moving within a bounded environment
encounter one another and collide.

We introduced a rule through which their interaction generates a third, smaller object.


$$
A+B\rightarrow c
$$

The resulting c becomes part of the environment. It moves independently, encounters other
objects, and can participate in subsequent interactions that generate further objects.

From these initial conditions, the experiment develops an expanding population with
increasingly complex trajectories and histories.

[established] The computational experiments demonstrate that a small set of interaction rules
can produce a continuing sequence of generation, movement, collision, and state transformation.
Each generated object can be associated with the interaction that produced it.

The progression remains observable as the environment develops from two dimensions to three,
and as additional observers are introduced.

The addition of time as a fourth coordinate allows each event to be identified by where and when
it occurs. An object's present condition can therefore be connected to the earlier events that
contributed to its history.

The introduction of multiple observers makes another relationship visible.

D1, D2, and D3 encounter the same generated c at different positions and moments. Each
encounter is recorded independently, while the object's origin remains associated with the
original A–B collision.

The resulting records demonstrate how a common originating event can be connected to multiple
observations distributed through space and time.
### 8.2 The significance of a shared event
The traffic accident example gives this relationship an everyday meaning.

Two vehicles collide, producing an event with physical consequences and a developing history.

A bystander witnesses the occurrence. A traffic officer examines the sequence of events. An
insurance adjuster examines the resulting damage and financial consequences.

Each encounters information associated with the same accident.

Their questions may differ because they are examining different relationships within the event's
history.

The bystander may establish information about the condition of the people involved. The officer
may establish information about how the collision occurred. The adjuster may establish
information about the resulting damage.

These accounts concern one originating event.

The information formed by each observer reflects the questions investigated, the evidence
available, and the relationships established through that inquiry.

This example makes an important distinction visible: the history of an event and the
information an observer forms about that event are connected, while remaining
distinguishable.

The event provides a shared subject of inquiry. The observer's question determines which
relationship becomes the focus of investigation.

Information established through that investigation may subsequently become part of another
interaction, contributing to further questions and understandings.
### 8.3 The potential of a question
The original collision produces c before an observer asks anything about it.

The generated object has a position, a state, and an originating history. Those properties provide
possible subjects for later inquiry.

An observer might ask where c originated, how it reached its present location, or what happened
during its subsequent interactions.

The questions arise in relation to something whose history began earlier.

[conjecture] We propose that the resulting c represents the potential of a question: a state
produced through interaction that may subsequently become the subject of an observer's inquiry.

The potential belongs to the progression initiated by the originating interaction.

A question arises when an observer directs inquiry toward a relationship concerning that
potential.

The observer may encounter c without asking a question. The potential remains part of the
developing system regardless of whether inquiry occurs.

When a question does arise, it establishes a particular relationship between the observer and the
information associated with c.

The question may concern the object's origin, condition, movement, or history. Different
observers may investigate different relationships concerning the same object.

The resulting information becomes part of each observer's understanding.

This gives the proposed relationship a progression that can be examined:

Interaction → resulting state → developing history → observation → possible inquiry →
information formation.

The computational experiments make the originating interaction, resulting state, developing
history, and observer encounters visible. The theoretical investigation considers how questions
and information formation may develop from those conditions.
### 8.4 Information and the observer's reality
The relationship between different observers and a shared event leads to the central proposition
of this paper.

An observer encounters an event through information available at a particular position and time.

The observer may ask a question concerning that event. The question directs attention toward a
specific relationship, and the resulting investigation may establish information that contributes to
the observer's understanding.

Another observer may ask a different question concerning the same event and form a different
understanding.

Both understandings remain connected to the common history of the originating occurrence.

[conjecture] The formation of information through an observer's question may contribute
to what that observer recognizes as a form of reality.

The investigation uses a form of reality to describe an event as it becomes recognizable and
understandable through the information formed by an observer.

The bystander, traffic officer, and insurance adjuster each develop an informational
understanding of the accident.

Those understandings arise through different questions and may concern different relationships
within the same event.

The existence of multiple understandings is compatible with a common originating history. Each
observer's account can contribute information about that history while remaining distinct from
the accounts formed by others.

The proposition therefore concerns the relationship between an event, the observer's inquiry, and
the information through which that event becomes understood.

It offers a way to investigate the formation of observer-specific informational realities without
requiring a prior universal definition of reality.
### 8.5 Final conclusion
What began as two moving objects became a system containing successive generations of
interactions, transformations, and traceable histories.

The visual progression revealed how simple rules could generate a developing structure whose
individual events remained identifiable even as the accumulated movement became increasingly
complex.

Introducing multiple observers added distinct histories of encounters with the same generated
object.

The experiments made it possible to follow a result from its originating interaction through later
events and observations.

From this observable progression, the investigation developed a theoretical interpretation
concerning the potential of a question and the formation of information through inquiry.

The originating interaction produces a result that may become the subject of a question. The
observer encounters that result through its available information and may direct inquiry toward a
particular relationship within its history.

Different observers may ask different questions, establish different information, and develop
distinct understandings concerning the same event.

The central proposition is that what an observer recognizes as a form of reality may arise
through the information formed in the observer's relationship with an event.

The computational experiments provide a reproducible visual foundation for examining the
originating interactions and subsequent observations. The theoretical proposition extends that
examination to questions, information, and observer-specific understanding.

The resulting research offers a framework for investigating how the potential for inquiry arises
through interaction and how questions may participate in forming what an observer understands
about the world.

It leaves the reader with a question that follows directly from the experimental progression:

If an event has a history independent of its observers, and each observer can form different
information about that event through inquiry, what is the relationship between the event
itself and the reality each observer comes to recognize?

---

*Bruce Tisler is a researcher at Quantum Inquiry, where his work spans formal epistemology, AI safety, and multi-agent systems research.*

**AI Collaboration Disclosure**

This paper was developed in collaboration with artificial intelligence to assist with research synthesis, structural editing, and the clarification of complex mathematical arguments. While the tools aided the process, the final interpretations, perspectives, and the underlying thesis are a product of human inquiry.

**Keywords**

Quantum Cognition • Entropy and Inquiry • Systems Thinking • Cognitive Field Theory • Philosophy of Mind • Recursive Systems • Narrative Intelligence • Artificial Intelligence

http://www.linkedin.com/in/bruce-tisler

Quantum Inquiry: https://quantuminquiry.org

© 2026 Bruce Tisler
