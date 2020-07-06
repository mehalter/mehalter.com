---
#=== HTML OPTIONS ===#
theme: "#545963"
icons: icon
button:
    - name: "<i class=\"fab fa-keybase\"></i>"
      url:    https://keybase.io/mehalter
    - name: "<i class=\"fas fa-graduation-cap\"></i>"
      url:    https://scholar.google.com/citations?user=yMme7wkAAAAJ&hl=en
    - name: "<i class=\"fab fa-linkedin-in\"></i>"
      url:    https://www.linkedin.com/in/mehalter
    - name: "<i class=\"fab fa-git\"></i>"
      url:    https://git.mehalter.com/mehalter
    - name: "<i class=\"far fa-calendar-alt\"></i>"
      url:    https://drive.mehalter.com/index.php/apps/calendar/p/5xJkqitQMFjXqgZe/Personal
    - name: "<i class=\"fas fa-dna\"></i>"
      url:    promethease.html
    - name: "<i class=\"fas fa-book\"></i>"
      url:    https://mysecondbra.in
resume:
    - name: Printable CV
      url: resume.pdf
    - name: Man Page
      url: micah.1.html

#=== MAN PAGE OPTIONS ===#
lower: micah
upper: MICAH
flag:
    - name: student
    - name: employee
    - name: admin
      option:
          - systems
          - databases
    - name: developer
    - name: researcher

#=== GENERAL DETAILS ===$
name: Micah Elliot Halter
picture: images/micah.jpeg
location: Atlanta, GA
phone: +1 704 490 9840
email: micah@mehalter.com
url: mehalter.com
git:
    url: git.mehalter.com
    user: mehalter

keyserver:
    - fingerprint: BEB8 056E 542A 33EB 8A4B 081F 723F 998E 98D9 3D50
      url: http://keys.gnupg.net/pks/lookup?op=vindex&fingerprint=on&search=0x723F998E98D93D50
    - fingerprint: 4AC9 4692 18E3 1BCE 147F 1060 E51C 3EA3 BEB5 D4A9
      url: http://keys.gnupg.net/pks/lookup?op=vindex&fingerprint=on&search=0xE51C3EA3BEB5D4A9

#=== DESCRIPTIONS ===#
tagline: "a developer, researcher, and bartender"

summary: "I’m a <strong>computer science researcher</strong> at the <strong>Georgia Tech Research Institute</strong> in Atlanta, Georgia."

about-me: "I have been interested in computer science since I was six years old, and have built up an unmatched passion for the field. I have extensive experience in software development and research from internships, projects, and competitions. I graduated from the Georgia Institute of Technology with a Bachelor of Science in Computer Science with a focus in system architecture and theory, and am working as a Researcher at the Georgia Tech Research Institute."

description:
    sys-admin: "Through work opportunities and personal projects, I have had extensive experience with the configuration, hardening, and maintenance of various Linux distributions, including:"
    database-admin: "Through my work experiences I have become skilled in many database languages including MySQL, PostgreSQL, SQLite, and SQL Server. These experiences range from designing a full database schema, administrating and managing an existing database, and writing queries to parse through the data."
    developer: "I have worked on several development projects in both work environments and personally using a plethora of different programming languages and paradigms"
    researcher: "While working at the Georgia Tech Research Institute, I have found that I love being involved with research projects. I enjoy taking charge of open ended questions and exploring new methods and ways of tackling tough problems."


#=== EDUCATION ===#
education:
    - start: Jan&nbsp;2020
      end: Dec&nbsp;2021
      degree: Master of Science in Computer Science
      school: Georgia Institute of Technology
      id: git
      location: Atlanta, GA
      notes:
          - "Specialization in Machine Learning"
    - start: Aug&nbsp;2015
      end: May&nbsp;2019
      degree: Bachelor of Science in Computer Science
      school: Georgia Institute of Technology
      id: git
      location: Atlanta, GA
      notes:
          - "Concentration in system architecture and theory"
          - "Dean's List Fall 2015, Spring 2016, Fall 2016, Fall 2018, Spring 2019"
    - start: Aug&nbsp;2017
      end: Dec&nbsp;2017
      degree: Bachelor of Science in Computer Science
      school: Hong Kong University of Science and Technology
      id: hkust
      location: Hong Kong
      notes:
          - "Studied abroad"


#=== WORK EXPERIENCE ===#
experience:
    - company: Georgia Tech Research Institute
      position:
          - title: Research Scientist
            company: Georgia Tech Research Institute
            start: Jun&nbsp;2019
            end: Present
            id: gtri
            location: Atlanta, GA
            notes:
                - "Lead contributor to research projects sponsored by large entities DARPA, NIH, DOD, and ONR"
                - "Wrote and published peer reviewed conference and journal papers to communicate research findings to the greater research community"
                - "Contributed and participated in white paper and proposal writing to bring in more funding for new and on-going projects"
                - "Delivered applied research projects to sponsors such as source code, web applications, and technical reports"
                #- "Used NetFlow data and machine learning in Python and scikit-learn to detect compromised machines on a network based off known blacklists and whitelists of IP addresses"
          - title: Undergraduate Research Assistant
            company: Georgia Tech Research Institute
            start: Jan&nbsp;2016
            end: May&nbsp;2019
            id: gtri
            location: Atlanta, GA
            notes:
                - "Lead contributor to research projects sponsored by large entities NIH and ONR"
                - "Wrote and published a peer reviewed journal paper to communicate research findings to the greater research community"
                - "Delivered applied research projects to sponsors such as source code, web applications, and technical reports"
                - "Predicting crimes in Portland, OR using temporal and geographic features derived from crime statistics and GIS data"
    # - company:    Kindred Spirits Atlanta, LLC
    #   position:
    #       - title: Co-Owner
    #         company: Kindred Spirits Atlanta, LLC
    #         start:      Dec&nbsp;2018
    #         end:            Present
    #         id:             kindred-spirits
    #         location: Atlanta, GA
    #         notes:
    #             - "Manage infrastructure, logistics, and services for contracted catering events"
    #             - "Engage with customers and provide outstanding service to build customer relations and increase company value"
    #             - "Maintain and file all necessary legal documents to ensure legitimacy of the business"
    - company: The Boeing Company
      position:
          - title: Software Development Intern
            company: The Boeing Company
            start: May&nbsp;2016
            end: Aug&nbsp;2017
            id: boeing
            location: Kent, WA
            notes:
                - "Developed a security auditing tool suite for Red Hat Enterprise Linux 7 to maintain hardened security on classified servers"
                - "Developed a web application in C#, HTML, and JavaScript to view and analyze network traffic"
                - "Developed several system administration scripts as needed by team members to complete tasks such as emailing system logs and automatic server backups"
                - "Organized and led a software development team to create a minimum viable product of a Kanban board web application"
                - "Pitched the Kanban board prototype to management to form a team to continue development of the application after I left"
                - "Documented and executed an upgrade plan for the company's identity management servers"
                - "Developed an Outlook-integrated conference room mapping tool in C#"
    # - company:    The Boeing Company
    #       position:
    #           - title: Software Development Intern
    #               start:      May&nbsp;2016
    #               end:            Aug&nbsp;2016
    #               id:             boeing
    #               location: North Charleston, SC
    #               notes:
    #                   - "Organized and led a software development team of five in a three day coding sprint to create a minimum viable product of a Kanban board web application"
    #                   - "Pitched the Kanban board prototype to management to form a team to continue development of the application after I left"
    #                   - "Documented and executed an upgrade plan for the company's identity management servers"
    #                   - "Developed an Outlook-integrated conference room mapping tool in C#"
    #- company:  North Carolina Statue University College of Textiles
    #  position:
    #        - title: Wearable Technology Research Intern
    #            start:      Jun&nbsp;2014
    #            end:            Aug&nbsp;2014
    #            id:             ncsu
    #            location: Raleigh, NC
    #            notes:
    #                - "Conducted research on a cooling vest, the Porticool, by the company Porticos"
    #                - "Integrated a self-powered electrical system of thermelectric generatos to power various sensors"


#=== PROJECTS ===#
project:
    - name: AlgebraicJulia
      id: algebraicjulia
      type: Georgia Tech Research Institute
      repo: https://github.com/AlgebraicJulia
      logo: images/algebraicjulia.png
      notes:
          - "A GitHub Organization for a collection of Julia packages for defining modeling frameworks as generalized algebraic theories"
          - "Includes Julia packages such as Catlab.jl, AlgebraicPetri.jl, and AlgebraicRelations.jl"
          - "A category theory approach to defining metamodeling tasks for representing, composing, selecting, and tuning scientific models"
          - "Research funded by the Defense Advanced Research Projects Agency (DARPA)"
    - name: Petri.jl
      id: petri.jl
      type: Software Development
      repo: https://github.com/mehalter/Petri.jl
      logo: images/petri.png
      notes:
          - "A stochastic petri net modeling framework for the Julia programming language"
          - "Allow petri nets to be compiled to Gillespie and differential equation based simulations"
    - name: VirtualEnv.jl
      id: virtualenv.jl
      type: Software Development
      repo: https://github.com/mehalter/VirtualEnv.jl
      notes:
          - "Self-contained virtual environments for the Julia programming language"
          - "A reimplementation of `venv` from Python in Julia"
    - name: Corsair Database
      id: corsair
      type: Georgia Tech Research Institute
      notes:
          - "Research funded by the Office of Naval Research (ONR)"
          - "Developed a web application for viewing and analyzing sonar SAS data using Go, Python, and PostgresDB deployed with Docker and Drone.io"
          - "Engineered a database for managing scientific experiments to utilize the speed and efficiency of using a rigid relational database, while being flexible enough to handle the changing data requirements of scientific experimentation"
    #- name:    Linux Configuration
    #  id:      linux
    #  type:    System Administration
    #  repo:    https://git.mehalter.com/mehalter/dotfiles
    #  image: images/desktop.png
    #  notes:
    #        - "Configured and maintain a minimal Linux installation to meet my development needs"
    #        - "Developed many custom scripts to optimize my workflow"
    #- start: Sep&nbsp;2016
    #  end:     Nov&nbsp;2016
    #  name:    Clean Water Crowdsourcing
    #  id:      clean-water
    #  type:    Software Development
    #  repo:    https://git.mehalter.com/mehalter/Clean-Water-Crowdsourcing
    #  notes:
    #        - "Completed the full-stack development process from design to implementation of a full Java based application"
    #        - "Demonstrated good development practices to make sure code is concise, maintainable, and sharable"
    #- start: May&nbsp;2015
    #  name:    Huffman Coding
    #  id:      huffman-coding
    #  type:    Software Development
    #  repo:    https://git.mehalter.com/mehalter/Huffman-Coding-C
    #  notes:
    #        - "Programmed a C-based implementation of the Huffman coding compression and decompression algorithm"
    #- start: Aug&nbsp;2014
    #  end:     Apr&nbsp;2015
    #  name:    Verificia
    #  id:      verificia
    #  type:    Software Development
    #  notes:
    #        - "Designed a new security method to protect against key-loggers, mouse-trackers, and screen-grabbers"
    #        - "Developed and deployed a working prototype as a proof of concept"
    #        - "Pitched the idea through a business protfolio and presentation to investors and competition judges"
    #        - "Achieved finalist status in the competition as a Pete Conrad Summit Diplomat"
    #- start: Feb&nbsp;2015
    #  name:    Multi-Player Conway's Game of Life
    #  id:      conways
    #  type:    Software Development
    #  repo:    https://git.mehalter.com/mehalter/Multiplayer-Game-of-Life
    #  notes:
    #        - "Developed a Java-based version of Conway's Game of Life"
    #        - "Created and implemented new rules to the automaton to introduce competition between two cell strains"

publication:
    - type:  Peer Reviewed Conference Publications
      id: conf
      entries:
          - title: "Compositional Scientific Computing with Catlab and SemanticModels"
            authors: "**Micah Halter**, Evan Patterson, Andrew Baas, James Fairbanks"
            issue: "Applied Category Theory, 2020"
            links:
                - title: "PDF"
                  url: "https://arxiv.org/abs/2005.04831"
          - title: "SemanticModels.jl: A Julia Package for Scientific Model Augmentation"
            authors: "**Micah Halter**, Sreenath Raparti, Kun Cao, Christine Herlihy, James Fairbanks"
            issue: "JuliaCon, 2019"
            links:
                - title: "Slides"
                  url: "http://jpfairbanks.net/doc/slides/juliacon2019/slides.slides.html#/"
                - title: "Video"
                  url: "https://www.youtube.com/watch?v=WJneK7OjqMQ"
          - title: "A Compositional Framework for Scientific Model Augmentation"
            authors: "**Micah Halter**, Christine Herlihy, James Fairbanks"
            issue: "Applied Category Theory, 2019"
            links:
                - title: "PDF"
                  url: "https://arxiv.org/abs/1907.03536"
                - title: "Slides"
                  url: "http://jpfairbanks.net/doc/slides/act/slides.slides.html#/"
    - type:  Under Review Journal Publications
      id: journal-pend
      entries:
          - title: "Accelerating Automatic Target Recognition Performance Estimation with a Relational Database for Synthetic Aperture Sonar"
            authors: "James Fairbanks\\*, **Micah Halter**\\*, Trevor Goodyear, Matthew Jackson, Brian O’Donnell, John Wilcher"
            issue: "Navy Journal of Underwater Research, 2018"
    #- type:  Under Review Conference Publications
    #  id: conf-pend
    #  entries:

talk:
    - type: Posters
      id: poster
      entries:
          - title: "SemanticModels.jl: A Framework for Automatic Composition of Scientific Models Across Domains"
            speakers: Micah Halter, Kun Cao, James Fairbanks
            event: SIAM Conference on Parallel Processing for Scientific Computing
            date: Feb&nbsp;2020
            links:
                - title: "PDF"
                  url: "documents/siam-pp20.pdf"
          - title: Scientific Knowledge Extraction, Augmentation & Analysis
            speakers: Micah Halter, James Fairbanks, Eric Davis, Clayton Morrison, Ryan Wright
            event: DARPA Demo Day
            date: Sep&nbsp;2019

funding:
    - start: 2020
      end: 2021
      role: Task Lead
      sponsor: DARPA
      title: Computable Models - Generalized Algebraic Theories for Enhancing Multiphysics
      # agreement: Agreement No. HR00112090067
      amount: $\approx$$1M
    - start: 2019
      end: 2021
      role: Performer
      sponsor: Office of Naval Research
      title: Extracting, Explaining, and Estimating Information in Sonar Data
      # agreement: Contract No. N00014-19-C-2069
      amount: $\approx$$400K
    - start: 2019
      end: 2021
      role: Performer
      sponsor: Office of Naval Research
      title: MCM Situational Awarness
      # agreement: Contract No. N00014-16-C-3041 as ammended by P00009
      amount: $\approx$$375K
    - start: 2018
      end: 2020
      role: Task Lead
      sponsor: DARPA
      title: Artifical Intelligence Exploration - Automating Scientific Knowledge Extraction
      # agreement: Agreement No. HR00111990008
      amount: $\approx$$1M
    - start: 2018
      end: 2019
      role: Performer
      sponsor: Air Force
      title: Network Risk Indication
      # agreement: Contract No. FA8773-17-D-0004
      amount: $\approx$$135K
    - start: 2016
      end: 2019
      role: Performer
      sponsor: Office of Naval Research
      title: Performance Estimation of Underwater MCM Operations
      # agreement: Contract No. N00014-16-C-3041
      amount: $\approx$$990K
    - start: 2015
      end: 2019
      role: Performer
      sponsor: Office of Naval Research
      title: Automation for UxV-based Mine Countermeasures
      # agreement: Contract No. N00014-15-C-5172
      amount: $540K

open-source:
    - type: "Core Maintainer"
      id: "maintainer"
      entries:
        - repo: "AlgebraicJulia"
          url: "https://github.com/AlgebraicJulia"
        - repo: "Petri.jl"
          url: "https://github.com/mehalter/Petri.jl"
        - repo: "VirtualEnv.jl"
          url: "https://github.com/mehalter/VirtualEnv.jl"
        - repo: "XDGSpec.jl"
          url: "https://github.com/mehalter/XDGSpec.jl"
    - type: "Contributor"
      id: "contributor"
      entries:
        - repo: "Neovim"
          url: "https://github.com/neovim/neovim"
        - repo: "IJulia.jl"
          url: "https://github.com/JuliaLang/IJulia.jl"
        - repo: "qutebrowser"
          url: "https://github.com/qutebrowser/qutebrowser"
        - repo: "vim-pandoc"
          url: "https://github.com/vim-pandoc/vim-pandoc"
        - repo: "voidrice"
          url: "https://github.com/LukeSmithxyz/voidrice/"
    - type: "Arch User Repository Package Maintainer"
      id: "aur-packages"
      entries:
        - repo: "Ruby on Rails"
          url: "https://aur.archlinux.org/packages/ruby-rails/"
        - repo: "OpenSCAP"
          url: "https://aur.archlinux.org/packages/openscap/"
        - repo: "Translate Shell"
          url: "https://aur.archlinux.org/packages/translate-shell-git/"
        - repo: "Antigen"
          url: "https://aur.archlinux.org/packages/antigen/"
        - repo: "MyEtherWallet"
          url: "https://aur.archlinux.org/packages/myetherwallet/"
        - repo: "HTTP Prompt"
          url: "https://aur.archlinux.org/packages/http-prompt/"
        - repo: "Ueberzug"
          url: "https://aur.archlinux.org/packages/python-ueberzug-git/"


#=== SKILLS ===#
skill:
    - line:
        - Full Stack Development
        - Deep Learning
        - System Administration
        - Database Design and Management
    - line:
        - High Performance Computing
        - Machine Learning
        - Functional Programming
        - Category Theory

language:
    - C/C++
    - Julia
    - Python
    - Go
    - Java
    - Haskell
    - Scala
    - Perl
    - Bash
    - SQL
    - MySQL
    - PostgreSQL
    - LaTeX
    - HTML
    - CSS
    - JavaScript

operating-system:
    - Red Hat Enterprise Linux
    - Debian, Ubuntu
    - Arch Linux


#=== COMMUNITY INVOLVEMENT ===#
community:
    - start: Aug&nbsp;2015
      end:     May&nbsp;2019
      name:  Georgia Tech's Men's Ultimate Frisbee
      place: Georgia Institute of Technology
      notes:
          - "Help with recruitment and teaching new players"
    #- start: Aug&nbsp;2015
    #  end:     May&nbsp;2017
    #  name:    TEDxGeorgiaTech
    #  place: Georgia Institute of Technology and TED
    #  notes:
    #        - "Organized an official TEDx university even with a group of students at Georgia Tech"
    #        - "Designed all of the visuals for the conference, including rewriting the event website TEDxGeorgiaTech.com"
    #- start: Aug&nbsp;2013
    #  end:     Jun&nbsp;2015
    #  name:    Research Triangle Google Development Group
    #  place: Google
    #  notes:
    #        - "Competed in various hack-a-thon events hosted by Google and won the Android Wear hack-a-thon"
    #        - "Participated in code labs wth the group to explore technologies like Dart language and AngularJS"


#=== ADDITIONAL NOTES ===#
additional-notes:
    - "Outside of the field of computer science I have many hobbies and passions including Ultimate Frisbee, coffee, and music."
    - "At Georgia Tech and the greater Atlanta area, I am a very active member of the Ultimate Frisbee community. This includes playing on multiple competitive teams throughout the years and competing in tournaments nationally and globally."
    - "I have been an avid coffee enthusiast for several years, frequenting many coffee shops, getting to know local coffee roasters and baristas, and hand brewing my own craft coffee."
    - "Growing up I was very involved with band and played many instruments including piano and flute. Nowadays I don’t play very often, but love to attend concerts and live music events."
---
