const form = document.querySelector("#form");
      form.addEventListener("submit", (e) => {
        e.preventDefault();
        const query = form.elements.query.value;

        fetch("/palette", {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
          method: "POST",
          body: new URLSearchParams({
            query: query,
          }),
        })
          .then((response) => response.json())
          .then((data) => {
            const colors = data.colors;

            const container = document.querySelector(".container");
            container.innerHTML = "";

            for (const color of colors) {
              const div = document.createElement("div");
              div.classList.add("color");
              div.style.backgroundColor = color;
              div.style.width = `calc(100% / ${colors.length})`;

              const titlespan = document.createElement("span");
              titlespan.innerHTML = color;
              div.appendChild(titlespan);

              div.addEventListener("click", (e)=>{
                navigator.clipboard.writeText(color)
                
              })

              container.appendChild(div);   
            }
          });
      });