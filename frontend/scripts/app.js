import "htmx.org";
import Alpine from "alpinejs";

window.Alpine = Alpine;
Alpine.start();

Alpine.data("comment_form", () => ({
  init() {
    console.log(123);
  },
}));
