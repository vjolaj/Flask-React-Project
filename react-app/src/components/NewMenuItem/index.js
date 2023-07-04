// import React, { useState, useEffect } from "react";
// import { useDispatch, useSelector } from "react-redux";
// import { Redirect, useHistory } from "react-router-dom";
// import './NewMenuItem.css';

// function NewMenuItemPage() {
//     const sessionUser = useSelector((state) => state.session.user);
//     const [itemName, setItemName] = useState("");
//     const [price, setPrice] = useState("");
//     const [image, setImage] = useState(null);
//     const [imageLoading, setImageLoading] = useState(false);
//     const [itemType, setItemType] = useState("");
//     const [description, setDescription] = useState("")
//     const dispatch = useDispatch();
//     const history = useHistory();


//     const handleSubmit = async (e) => {
//       e.preventDefault();
//       const formData = new FormData();
//       formData.append("itemName", itemName)
//       formData.append("price", price)
//       formData.append("itemType", itemType)
//       formData.append("description", description)
//       formData.append("imageUrl", image);
//       // aws uploads can be a bit slow—displaying
//       // some sort of loading message is a good idea
//       setImageLoading(true);
//       await dispatch(createPost(formData));
//       history.push("/images");
//     };
  
//     return (
//       <>
//         <form onSubmit={handleSubmit} className="addMenuItem-Form">
  
//           <ul>
//             {errors.map((error, idx) => <li key={idx}>{error}</li>)}
//           </ul>
//           <p>Add a new menu item</p>
//           <label>
           
//             <input
//               type="text"
//               value={itemName}
//               onChange={(e) => setItemName(e.target.value)}
//               required
//               placeholder="Enter Item Name"
//               className="input"
//             />
//           </label>
//               <select>
//                     <input
//                           type="decimal"
//                           value={price}
//                           onChange={(e) => setPrice(e.target.value)}
//                           required
//                           placeholder="Enter price"
//                           className="input"
//                       />
//                   </select>
//           <label>
           
//             <input
//               type="text"
//               value={description}
//               onChange={(e) => setDescription(e.target.value)}
//               required
//               placeholder="Item Description"
//               className="input"
//             />
//           </label>
//           <div className='form-input-box'>
//                         <label 
//                             className="form-label" 
//                             htmlFor='image'
//                         >
//                             Post Image:
//                         </label>
//                         <input
//                             id="image"
//                             type="file"
//                             accept="image/*"
//                             onChange={(e) => setImage(e.target.files[0])}
//                             >
//                         </input>
//                     </div>
//           <button type="submit" className="logIn-form-button">Sign Up</button>
//         </form>
//       </>
//     );
//   }
  
//   export default NewMenuItemPage;
  