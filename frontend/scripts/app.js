import "htmx.org";
import Alpine from "alpinejs";

Alpine.data("comment_form", () => ({
  content: "",
}));

Alpine.start();
