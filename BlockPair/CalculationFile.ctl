; All values in 100 nm units
(define L 1.5) ; Side Length of the nanocube
(define G 0.2) ; Gap between particles
(define pi 3.1415926)
(define theta (* pi (/ 45.0 180.0))); Particle angle from vertical
(define wvlngth 6.2) ; Wavelength of laser light

; I Don't anticipate you needing to change anything below here, but it's commented in case you do

; Define the center coordinates of the blocks
(define centerRx  (+ (*  (* (/ 1.0 (sqrt 2.0)) L) (cos (+ theta (/ pi 4.0) (* 3.0 (/ pi 2.0)) )) ) (/ G 2.0) ))
(define centerRy  (*  (* (/ 1.0 (sqrt 2.0)) L) (sin (+ (/ pi 4.0) theta (* 3.0 (/ pi 2.0)) )) ))

(define centerLx (* -1.0 (+ (*  (* (/ 1.0 (sqrt 2.0)) L) (cos (+ (/ pi 4.0) theta (* 3.0 (/ pi 2.0)) )) ) (/ G 2.0) )) )
(define centerLy (*  (* (/ 1.0 (sqrt 2.0)) L) (sin (+ theta (/ pi 4.0) (* 3.0 (/ pi 2.0)) )) ))

; Set up the calculation grid
(set! geometry-lattice
        (make lattice
                (size 20.0 20.0 no-size)
        )
)

; Resolution
(set! resolution 40)

; Construct the metallic block objects, currently set to silver
(set! geometry
        (list
                (make block
                        (center centerRx centerRy)
                        (size L L )
                        (e1 (cos theta) (sin theta)  )
                        (e2 (sin theta) (* -1.0 (cos theta)) )
                        (material
                (make dielectric
                    (epsilon 1.000001)
                                        (polarizations
                                                (make polarizability
                                                        (omega 8.06554724676e-22)
                                                        (gamma 0.00387146267844)
                                                        (sigma 6.85971845e+41)
                                                )
                                                (make polarizability
                                                        (omega 0.0658148655336)
                                                        (gamma 0.313427166009)
                                                        (sigma 7.92469618056)
                                                )
                                                (make polarizability
                                                        (omega 0.361417172127)
                                                        (gamma 0.0364562735554)
                                                        (sigma 0.501327328096)
                                                )
                                                (make polarizability
                                                        (omega 0.660165042147)
                                                        (gamma 0.00524260571039)
                                                        (sigma 0.013329225019)
                                                )
                                                (make polarizability
                                                        (omega 0.732593656423)
                                                        (gamma 0.0738804127803)
                                                        (sigma 0.826552111457)
                                                )
                                                (make polarizability
                                                        (omega 1.63649953637)
                                                        (gamma 0.195105587899)
                                                        (sigma 1.11333628042)
                                                )
                                        )
                )
            )
                )
                (make block
                        (center centerLx centerLy)
                        (size L L )                     (e1 (* -1.0 (cos theta)) (sin theta) )
                                                        (e2 (* -1.0 (sin theta)) (* -1.0 (cos theta)
                        ) )
(material
                (make dielectric
                    (epsilon 1.000001)
                                        (polarizations
                                                (make polarizability
                                                        (omega 8.06554724676e-22)
                                                        (gamma 0.00387146267844)
                                                        (sigma 6.85971845e+41)
                                                )
                                                (make polarizability
                                                        (omega 0.0658148655336)
                                                        (gamma 0.313427166009)
                                                        (sigma 7.92469618056)
                                                )
                                                (make polarizability
                                                        (omega 0.361417172127)
                                                        (gamma 0.0364562735554)
                                                        (sigma 0.501327328096)
                                                )
                                                (make polarizability
                                                        (omega 0.660165042147)
                                                        (gamma 0.00524260571039)
                                                        (sigma 0.013329225019)
                                                )
                                                (make polarizability
                                                        (omega 0.732593656423)
                                                        (gamma 0.0738804127803)
                                                        (sigma 0.826552111457)
                                                )
                                                (make polarizability
                                                        (omega 1.63649953637)
                                                        (gamma 0.195105587899)
                                                        (sigma 1.11333628042)
                                                )
                                        )
                )
            )
                )
        )
)

; Set up the light source
(set! sources
        (list

                (make source
                        (src
                                (make continuous-src
                                        (wavelength wvlngth)
                                        (start-time 0.0)
                                        (width 2.0)
                                )
                        )
                        (component Ex)
                        (center 0.0 -4.75 )
                        (size 10.0 0.0 )
                )
        )
)

; Set up absorbing boundary conditions
(set! pml-layers
    (list
        (make pml
            (thickness 5.0)
        )
    )
)

; Set all run parameters and define outputs
(run-until 50.0
        (to-appended "eps" (at-beginning output-epsilon))
        (to-appended "final_dpwr" (at-end output-dpwr))
        (to-appended "Ey"
                (at-every 0.5
                        (in-volume
                                (volume
                                        (center 0.0 0.0 )
                                        (size 10.0 10.0 )
                                )
                        output-efield-y
                        )
                )
        )
        (to-appended "Ex"
                (at-every 0.5
                        (in-volume
                                (volume
                                        (center 0.0 0.0 )
                                        (size 10.0 10.0 )
                                )
                        output-efield-x
                        )
                )
        )
        (to-appended "dpwr" (at-every 0.5 output-dpwr))
)